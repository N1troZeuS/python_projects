from PIL import Image

image = Image.open("main.jpg")
size = 60 

red, green, blue = image.split()
pixels_count = -40 

both_sides_crop_coordinates = (pixels_count / 2, 0, image.width-pixels_count / 2, image.height)

cropped_left_red_coordinates = (pixels_count, 0, image.width, image.height)
cropped_left_red_image = red.crop(cropped_left_red_coordinates)
cropped_both_sides_red_image = red.crop(both_sides_crop_coordinates)
cropped_red_image = Image.blend(cropped_left_red_image, cropped_both_sides_red_image, 0.5)

cropped_green_image = green.crop(both_sides_crop_coordinates)

cropped_right_blue_coordinates = (0, 0, image.width - pixels_count, image.height)
cropped_right_blue_image = blue.crop(cropped_right_blue_coordinates)
cropped_both_sides_blue_image = blue.crop(both_sides_crop_coordinates)

cropped_blue_image = Image.blend(cropped_right_blue_image, cropped_both_sides_blue_image, 0.5)

final_image = Image.merge("RGB", (cropped_red_image, cropped_green_image, cropped_blue_image))
final_image.save("ready.jpg")
final_image.thumbnail((size, size))
final_image.save("thumbnail.jpg")
print("\u001b[25A", end="")
print("Ready!")