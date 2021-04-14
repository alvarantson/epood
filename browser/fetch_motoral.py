from selenium import webdriver
import time
import json



webdriver_path = "C:\\Users\\Alvar\\Documents\\Repod\\epood\\app\\browser/chromedriver.exe"
main_url = "https://motoral.ee"


def login(driver):
	username = "info@fixuslasnamae.ee"
	password = "LASNA"
	
	driver.get("https://motoral.ee/et/catalog/login")
	driver.find_element_by_name('username').send_keys(username)
	driver.find_element_by_name('password').send_keys(password)
	driver.find_element_by_name('password').submit()

	return driver


def main_categories(driver):
	driver.get("https://motoral.ee/et/catalog/product")

	categories = driver.find_element_by_id("product-menu-list").find_elements_by_tag_name("li")

	main_categories = []
	for item in categories:
		main_categories.append(
				{
				"category": item.find_element_by_tag_name("a").text, 
				"url": item.find_element_by_tag_name("a").get_attribute('href'),
				"sub_categories": []
				}
			)
	return main_categories


# Kataloogi menüü
def kataloogi_menuu(driver, main_categories):
	for i in range(len(main_categories)):

		driver.get(main_categories[i]["url"])
		time.sleep(0.05)

		# Alaliigid
		for item_cat in driver.find_elements_by_class_name("element__sub-cat-menu-link"):

			if "Outlet" in item_cat.text:
				continue
			elif "Pakkumised" in item_cat.text:
				continue
			elif "Uued tooted" in item_cat.text:
				continue

			main_categories[i]["sub_categories"].append(item_cat.text)
	return main_categories


def products(driver, tooted, category):
	for product in driver.find_element_by_id("product-list").find_elements_by_tag_name("li"):
		# just not to waste time
		try:
			if product == driver.find_element_by_id("product-list").find_elements_by_tag_name("li")[1]:
				break
		except:
			break
		toode = {}
		product.find_element_by_class_name("prow__info-linkw").click()
		time.sleep(0.6)

		rows = driver.find_elements_by_class_name("dialog__data-row")

		toode["category"] = category
		for row in rows:
			try:
				label = row.find_element_by_class_name("dialog__label-col").text
			except:
				continue
			value = row.find_element_by_class_name("dialog__data-col").text
			
			toode[label] = value

		rows = driver.find_elements_by_class_name("c12")

		for row in rows:
			if "Lühiinfo" in row.text:
				toode["description"] = row.get_attribute('innerHTML')
				
		try:
			toode["image_url"] = driver.find_element_by_id("img-big").get_attribute("src")
		except:
			toode["image_url"] = ""

		tooted.append(toode)
		time.sleep(0.5)
		driver.find_element_by_class_name("closeText").click()
		time.sleep(0.4)
	return tooted
		

# Alaliigid - tooted
def alaliigid(driver, main_categories):
	tooted = []

	for item in main_categories:
		driver.get(item["url"])
		time.sleep(0.6)

		for wanted_cat in item["sub_categories"]:
			for j in range(len(driver.find_elements_by_class_name("element__sub-cat-menu-link"))):
				#print(wanted_cat, j.text, wanted_cat in j.text)
				if wanted_cat in driver.find_elements_by_class_name("element__sub-cat-menu-link")[j].text:
					print(item["category"],driver.find_elements_by_class_name("element__sub-cat-menu-link")[j].text)
					driver.find_elements_by_class_name("element__sub-cat-menu-link")[j].click()
					time.sleep(1)
					tooted = products(driver, tooted, [item["category"],wanted_cat])

#					for i in range(len(driver.find_elements_by_class_name("layout__paginationItem"))):
#						driver.find_element_by_class_name("layout__paginationItem").click()
#						time.sleep(0.6)
#						tooted = products(driver, tooted, [item["category"],wanted_cat])
							

					driver.get(item["url"]) # RESET INTO Alaliigid BROWSER
					time.sleep(1)
	return tooted








driver = webdriver.Chrome(webdriver_path)
driver = login(driver)
#main_categories = main_categories(driver)
#main_categories = kataloogi_menuu(driver, main_categories)
#with open("cats.txt", "w") as fm:
#	json.dump(main_categories, fm)

with open("cats.txt") as fm:
	main_categories = json.load(fm)
tooted = alaliigid(driver, main_categories)
with open("tooted.txt", "w") as fm:
	json.dump(tooted, fm)
#print(main_categories)