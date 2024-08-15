from machine import Pin, I2C
import ssd1306
import time

# Define the I2C interface and pins
i2c = I2C(1, scl=Pin(7), sda=Pin(6), freq=400000)  # Use appropriate pins
# 1 for pin i2C1 and 0 for pin i2C0

# Initialize the OLED display (0x3d is the common I2C address for SSD1306)
oled = ssd1306.SSD1306_I2C(128, 64, i2c, addr=0x3D)
# check the address according to the scanner addr=0xXX (0x3D commonly for ssd1309)

# Clear the display
oled.fill(0)

# Draw text
oled.text('Hello world', 4, 20)

# Update the display
oled.show()

# Keep displaying for 10 seconds
time.sleep(10)
