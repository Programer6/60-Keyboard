# 3D Printer Design: CAD & PCB Documentation
_Made by: @codelife / @programmer6_

| | |
|-------------------|-------------------|
| **Project Status** | Awaiting funding |
| **Total Time** | 25+ HOURS |
| **CAD Link** | 
| **Repository** | https://github.com/Programer6/60-Keyboard

---

June 18th, 2025 - 3.5 H
I spent most of the day in KiCad, laying out the schematic.
I designed a 5-row by 14-column key matrix. Each switch is paired with a 1N4148 diode to prevent "ghosting," which is when the keyboard thinks you've pressed keys you haven't. I also added support for two rotary encoders (for volume/scrolling) and two I2C connectors for OLED screens. 
I double-checked all my connections, and everything seems to be in order.


<img width="922" height="325" alt="Screenshot 2025-07-19 at 3 03 35 PM" src="https://github.com/user-attachments/assets/91b1a52a-3929-411d-830e-d3bd27bb1767" />

The plan is to use a Raspberry Pi Pico as the microcontroller because it's powerful, cheap, and has great community support with KMK firmware.
<img width="459" height="448" alt="Screenshot 2025-07-19 at 3 03 10 PM" src="https://github.com/user-attachments/assets/4712bb58-a9f2-4ab3-9b73-7d53c326902f" />

<img width="864" height="304" alt="Screenshot 2025-07-19 at 3 04 04 PM" src="https://github.com/user-attachments/assets/bac4f354-a012-40e6-b589-4181e977069b" />


<img width="1002" height="424" alt="Screenshot 2025-07-19 at 3 05 17 PM" src="https://github.com/user-attachments/assets/22eab528-b86b-4f33-9c43-80773d67c389" />
<img width="1019" height="345" alt="Screenshot 2025-07-19 at 3 06 17 PM" src="https://github.com/user-attachments/assets/6d174112-517e-426f-841f-51e136348ee9" />
<img width="672" height="537" alt="Screenshot 2025-07-19 at 3 17 49 PM" src="https://github.com/user-attachments/assets/927a9c1e-b539-4829-85b3-ea7f4366518e" />


June 19th - 2.5 H
Inical placing of the the components nothing wire as I realse that these is still some stugg to update in kicad & also add highway slikscreen!!
<img width="1135" height="545" alt="Screenshot 2025-07-19 at 3 54 30 PM" src="https://github.com/user-attachments/assets/e1bca1c0-d389-4b26-a561-48e0bb4a825a" />


<img width="988" height="674" alt="Screenshot 2025-07-22 at 3 07 54 PM" src="https://github.com/user-attachments/assets/6cae5e44-028c-4ac6-acfd-053b97d90547" />
Jun 20th -  3 H fix:
I started laying out the PCB today and immediately ran into a problem. While the Pi Pico has a lot of GPIO pins, my initial design used almost all of them, which was going to make routing the board a nightmare. 
To fix this, I decided to revise the schematic and add an MCP23017 GPIO expander

While I was at it, I fixed a few other issues. I had initially messed up the I2C connections for the OLED screens. I've now consolidated the entire I2C bus, so the GPIO expander and the two screen connectors (J1, J2) all share the same SCL and SDA lines, with the proper pull-up resistors. This was thankfully pointed out by LemonGravy!
<img width="738" height="437" alt="Screenshot 2025-07-22 at 3 11 16 PM" src="https://github.com/user-attachments/assets/528d92e7-473b-4cc8-a21b-d4cdd058492e" />


Routing - 21 June
I spent the entire day routing the PCB in KiCad e decision to use a GPIO expander yesterday really paid off, as it made the routing much more manageable. 

Here's the result of today's work:
<img width="1259" height="626" alt="Screenshot 2025-07-22 at 3 12 04 PM" src="https://github.com/user-attachments/assets/8e59cedd-7bce-45e0-9640-4e2a06265251" />


