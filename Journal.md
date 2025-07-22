# 3D Printer Design: CAD & PCB Documentation
_Made by: @codelife / @programmer6_

| | |
|-------------------|-------------------|
| **Project Status** | Awaiting funding |
| **Total Time** |  30 Hours |
| **CAD Link** | [Link to CAD Files] |
| **Repository** | https://github.com/Programer6/60-Keyboard |

---

## June 18, 2025 - Schematic Design (3.5 hours)
I spent most of the day in KiCad laying out the schematic for the keyboard.

I designed a 5-row by 14-column key matrix. Each switch is paired with a 1N4148 diode to prevent "ghosting," an issue where unintended key presses are registered. I also added support for two rotary encoders (ideal for volume control or scrolling) and two I2C connectors for optional OLED screens. After double-checking all connections, the initial schematic is complete.

<img width="922" height="325" alt="KiCad schematic of the key matrix with diodes" src="https://github.com/user-attachments/assets/91b1a52a-3929-411d-830e-d3bd27bb1767" />

The plan is to use a Raspberry Pi Pico as the microcontroller. It's powerful, affordable, and has excellent community support, particularly with the KMK firmware I intend to use.

<img width="459" height="448" alt="KiCad schematic of the Raspberry Pi Pico and its connections" src="https://github.com/user-attachments/assets/4712bb58-a9f2-4ab3-9b73-7d53c326902f" />

Here are the other detailed views from the schematic:

<img width="864" height="304" alt="KiCad schematic showing rotary encoder connections" src="https://github.com/user-attachments/assets/bac4f354-a012-40e6-b589-4181e977069b" />
<img width="1002" height="424" alt="KiCad schematic showing I2C connector details" src="https://github.com/user-attachments/assets/22eab528-b86b-4f33-9c43-80773d67c389" />
<img width="1019" height="345" alt="KiCad schematic showing another view of the key matrix" src="https://github.com/user-attachments/assets/6d174112-517e-426f-841f-51e136348ee9" />
<img width="672" height="537" alt="KiCad schematic overview" src="https://github.com/user-attachments/assets/927a9c1e-b539-4829-85b3-ea7f4366518e" />

---
## June 19, 2025 - Initial Component Placement (2.5 hours)
Started the initial placement of components on the PCB. I held off on routing the traces because I realized there were still a few things to update in the schematic, and I also want to add some custom silkscreen art.

<img width="1135" height="545" alt="Initial component placement in KiCad's PCB editor" src="https://github.com/user-attachments/assets/e1bca1c0-d389-4b26-a561-48e0bb4a825a" />
<img width="988" height="674" alt="Close-up of initial component placement" src="https://github.com/user-attachments/assets/6cae5e44-028c-4ac6-acfd-053b97d90547" />

---
## June 20, 2025 - Schematic Revision & GPIO Expander (3 hours)
I started laying out the PCB today and immediately ran into a problem. While the Pi Pico has a lot of GPIO pins, my initial design used almost all of them, which was going to make routing the board a nightmare.

To fix this, I revised the schematic to include an **MCP23017 GPIO expander**. This significantly reduces the number of pins required on the Pico, freeing up space and making the layout much cleaner.

While I was at it, I also fixed the I2C connections. Thanks to a suggestion from **LemonGravy**, I've consolidated the entire I2C bus. The GPIO expander and the two OLED screen connectors (J1, J2) now share the same SCL and SDA lines, with the proper pull-up resistors added.

<img width="738" height="437" alt="Revised schematic with the MCP23017 GPIO expander" src="https://github.com/user-attachments/assets/528d92e7-473b-4cc8-a21b-d4cdd058492e" />

---
## June 21, 2025 - PCB Routing (5 hours)
I spent the entire day routing the PCB in KiCad. The decision to use a GPIO expander yesterday really paid off, as it made the routing process much more manageable and resulted in a cleaner layout.

Here is the fully routed board:
<img width="1259" height="626" alt="Fully routed PCB in KiCad" src="https://github.com/user-attachments/assets/8e59cedd-7bce-45e0-9640-4e2a06265251" />

---
## June 22, 2025 - 3D Visualization & Case Design (7 hours total)

#### 3D Models in KiCad (3 hours)
I added 3D models for all the components in KiCad. This provides a realistic 3D preview of the finished PCB, which is crucial for verifying component placement and clearances before designing the case.
<img width="912" height="751" alt="3D view of the PCB in KiCad with all component models" src="https://github.com/user-attachments/assets/0bfc70dc-2301-4117-a2e4-269140e7fe88" />

#### 3D Printed Case Design (4 hours)
After finalizing the PCB, I exported the 3D model from KiCad and imported it into Fusion 360. I designed a simple and functional two-part case: a main body that holds the PCB and a top frame that acts as a switch plate and bezel.
<img width="983" height="582" alt="3D model of the keyboard case designed in Fusion 360" src="https://github.com/user-attachments/assets/01d4e48a-214e-4d0e-b626-b5e005a0509f" />

---
## June 23, 2025 - Firmware and Documentation (8 hours total)

#### KMK Firmware (5 hours)
I spent the day writing the firmware for the keyboard using KMK, a powerful CircuitPython-based firmware. I configured the key matrix, rotary encoders, and the I2C bus for the OLED screens. The initial firmware is now functional and ready for flashing.

#### Documentation & BOM (3 hours)
Finalized the project documentation by creating the Bill of Materials (BOM), organizing all progress logs and images, and writing this README file to document the entire process.
