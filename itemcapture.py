import requests
from bs4 import BeautifulSoup4
import psycopg2

# Proficiency Categories
proficiency_categories = ["Simple", "Martial", "Exotic", "Ammunition", "Firearms", "Mods", "Siege Engines", "Special"]

# Armor Categories
armor_categories = ["Light", "Medium", "Heavy", "Shields", "Extras", "Mods"]

# Misc Categories
misc_categories = ["AdventuringGear", "Alchemical Reagents", "Alchemical Remedies", "Alchemical Tools",
                   "Alchemical Weapons",
                   "Animal Gear", "Black Market", "Channel Foci", "Clothing", "Concoctions", "Dragoncraft",
                   "Dungeon Guides",
                   "Entertainment", "Food/Drink", "Fungal Grafts", "Herbs", "Kits", "Lodging/Services", "Mounts/Pets",
                   "Pathfinder Chronicles", "Spellbooks", "Tinctures", "Tools", "Torture Implements", "Transport, Air",
                   "Transport, Land", "Transport, Sea", "Vehicles"]

# Set up a database connection
try:
    conn = psycopg2.connect(database='pathfinder_loot_tracker', user='plt', password='alltheloot')
    cur = conn.cursor()
except psycopg2.Error as e:
    print("Error while connecting to PostgreSQL", e)


def scrape_data(base_url, categories, item_type):
    for category in categories:
        url = f"{base_url}?Category={category}"
        response = requests.get(url)
        soup = BeautifulSoup4(response.text, 'html.parser')

        # Identify the item categories
        item_categories = soup.find_all('h1')

        for category in item_categories:
            print(f"Category: {category.text.strip()}")

            # Each item's details are listed in the next sibling of the category
            items_list = category.find_next_sibling(text=True).strip().split('\n')

            for item in items_list:
                # Split item details by space but keep text within brackets as one group
                item_details = [x.strip() for x in item.split() if x.strip()]

                # Make sure the item_details list is not empty and contains both name and cost
                if item_details and len(item_details) >= 2:
                    name, real_value = item_details[0], item_details[1]

                    # Insert into PostgreSQL
                    try:
                        insert_query = """INSERT INTO itemref (name, real_value, type) VALUES (%s, %s, %s)"""
                        cur.execute(insert_query, (name, real_value, item_type))
                        conn.commit()
                    except psycopg2.Error as e:
                        print(f"Error while inserting data into PostgreSQL: {e}")

            print("\n")


# Scrape proficiency data
scrape_data("https://www.aonprd.com/EquipmentWeapons.aspx?Proficiency", proficiency_categories, "weapon")

# Scrape armor data
scrape_data("https://www.aonprd.com/EquipmentArmor.aspx", armor_categories, "armor")

# Scrape misc data
scrape_data("https://www.aonprd.com/EquipmentMisc.aspx", misc_categories, "gear")

# Close the cursor and connection
cur.close()
conn.close()
