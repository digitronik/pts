# -*- coding: utf-8 -*-
slots=[0, 555, 0, 9]

for s in slots:
    if s > 50:
        slots[slots.index(s)] = "Not Available"
    else:
        slots[slots.index(s)] = "Available"

msg = "Parking Slots : \n" +"Slot-1: "+slots[0]+"\n" + "Slot-2: "+slots[1]+"\n"+ "Slot-3: "+slots[2]+"\n"+ "Slot-4: "+slots[3]
#send_txt(chat_id, msg)
print slots

msg = "Available Slots \n"
for s_no, s in enumerate(slots, start=1):
    if s == "Available":
        msg +="slot: "+ str(s_no) +"\n"

print msg