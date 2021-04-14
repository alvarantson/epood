from urllib.request import urlopen

from .models import Product, Product_lang, Category
from navbar.models import Lang


def motoral_image_url(filename, alt_image = ""):
	if filename.count(".") > 1:
		filename = filename.replace(".", "_46_", 1)
	String = (
		"https://media.motoral.ee/productfiles/" +
		filename.replace(".jpg","").replace(".png","").replace(".JPG","").replace(".PNG","") +
		"/image/"
		)
	if alt_image != "":
		String += alt_image
	else: 
		String += filename

	return String


def import_motoral():
	key = "400ed9bd1846ce43a91860153d8aee99"
	url = "https://api.motoral.ee/product/export?token="+key

	added = 0
	updated = 0
	failed_to_add = 0

	response = urlopen(url)
	data = response.read().decode('utf-8')
	KM = 20 # 20% TODO: LIVE KM FROM DB

	data = str(data).split("\n")

	# PRINT COMPLETION %
	data_length = len(data)
	print("===============================")
	print("Total import:",data_length,"products")
	percentages = [i for i in range(0,data_length,int(data_length/20))]
	percentages2 = [str(i)+"%" for i in range(0,100,5)]

	# DATA PROCESSING
	for i in range(len(data)):
		if i in percentages:
			print(percentages2[percentages.index(i)],"completed!")
		
		try:
			# IF HEADER
			if "PRODUCT_IMAGE" in data[i]:
				continue

			cols = data[i].split("\",\"")
			cols[0] = cols[0].replace("\"","")
			cols[len(cols)-1] = cols[len(cols)-1].replace("\"","")

#			print(1)
			# IF PRODUCT EXISTS IN DB
#			try:
#				if Product_lang.objects.filter(product__code=cols[0]) != 0:
#					continue
#			except:
#				pass
#			print(2)

			more_images = []
			for item in cols[14].split("|"):
				more_images.append(motoral_image_url(cols[5]))
			try:
				code = cols[0]
			except:
				code = None

			try:
				price = float(cols[2])*((100+KM)/100)
			except:
				price = None

			try:
				stock = int(float(cols[3]))
			except:
				stock = None

			try:
				special_price = float(cols[4])
			except:
				special_price = None

			try:
				image_url = motoral_image_url(cols[5])
			except:
				image_url = None

			try:
				tracking_group = cols[6]
			except:
				tracking_group = None

			try:
				tracking_group_parent = cols[6].split("-")[0] + "-"
			except:
				tracking_group_parent = None

			try:
				EAN = cols[8]
			except:
				EAN = None

			try:
				brand_name = cols[9]
			except:
				brand_name = None

			try:
				brand_image_url = (
				"https://media.motoral.ee/images/brand_logo/" +
				cols[10]
				)
			except:
				brand_image_url = None

			try:
				measurements = cols[11]
			except:
				measurements = None

			try:
				items_in_package = cols[12]
			except:
				items_in_package = None

			try:
				weight = float(cols[13])
			except:
				weight = None

			try:
				more_images = more_images
			except:
				more_images = None

			if len(Product.objects.filter(code=code)) == 0:
				Product.objects.create(
					code = code,
					price = price,
					stock = stock,
	#				special_price = special_price, # IF WANTED BY US
					image_url = image_url,
					tracking_group = tracking_group,
					tracking_group_parent = tracking_group_parent,
					EAN = EAN,
					brand_name = brand_name,
					brand_image_url = brand_image_url,
					measurements = measurements,
					items_in_package = items_in_package,
					weight = weight,
					more_images = more_images
					)

				for lang in Lang.objects.all():
					# TODO: tõlge
					Product_lang.objects.create(
						lang = lang,
						product = Product.objects.get(code=code),
						name = cols[1],
						description = cols[15]
						)
				added += 1
			else: # UPDATE STOCK / PRICE, etc..
				item = Product.objects.get(code=code)
				if item.price != price or item.stock != stock:
					item.price = price
					item.stock = stock
					item.save()
					updated += 1

		except:
			print("FAILED IMPORT ROW: ", data[i])
			failed_to_add += 1

	print("100% completed!")
	print("added:",added,"updated:",updated,"failed_to_add:",failed_to_add)
	print("===============================")
	return (added, updated, failed_to_add)



def import_motoral_categories(lang = "et"):
	key = "400ed9bd1846ce43a91860153d8aee99"

	for lang in Lang.objects.all():

		url = "https://api.motoral.ee/product/category?token="+key+"&lang="+lang.lang

		response = urlopen(url)
		data = response.read().decode('utf-8')

		for row in data.split("\n"):
			try:
				if "CATEGORY" in row:
					continue

				cols = row.split("\",\"")
				cols[0] = cols[0].replace("\"","")
				cols[len(cols)-1] = cols[len(cols)-1].replace("\"","")

				Category.objects.create(
					lang = lang,
					code = cols[0],
					name = cols[1],
					parent = False
					)
			except:
				print("FAILED ROW:", row)