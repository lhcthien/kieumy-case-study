# WMS_project_MVC
Warehouse Management System realised in Python 3.10 Tkinter

The Warehouse Management System (WMS) provides ability to keep track of received incoming and outgoing products, to have a warehouse inventory of the stored stock. 
The system is developed as a MVC architecture using Tkinter(GUI) as front-end, and JSON file persistence technologies.

The main user roles (actors) are:
•	Warehouse Worker (WW) – view specific Receipts and Orders (only assigned to him/her), receive the incoming Receipts and send away the outgoing Orders, can change Location, send report to client (optional).
•	Client – can create Receipts and Orders, view old Receipts and Orders and stored stock
•	Administrator – can manage (create, update, delete) all Registered Users, cancel/delete Receipts and Orders, manage Products (create, update and delete), manage Locations (create, update and delete)
