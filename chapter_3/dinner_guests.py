guest_list = ['manuela','stefania','angelo']
print(f"You are invite to my dinner {guest_list[0].title()}")
print(f"You are invite to my dinner {guest_list[1].title()}")
print(f"You are invite to my dinner {guest_list[2].title()}")
print(f"Hello {guest_list[0].title()}, {guest_list[1].title()}, {guest_list[2].title()} you are invited!")
print(f"You are {len(guest_list)} invit.")
print("-------------------------------------------------------------")
guest_revok = 'stefania'
guest_list.remove(guest_revok)
guest_list.append('fabio')
print(f"The guest {guest_revok.title()} are revok your invitation!")
print("-------------------------------------------------------------")
print(f"The new guest list is {guest_list[0].title()}, {guest_list[1].title()}, {guest_list[2].title()}")
print(f"You are invite to my dinner {guest_list[0].title()}")
print(f"You are invite to my dinner {guest_list[1].title()}")
print(f"You are invite to my dinner {guest_list[2].title()}")
print(f"You are {len(guest_list)} invit")
print("-------------------------------------------------------------")
print(f"Hello {guest_list[0].title()}, {guest_list[1].title()}, {guest_list[2].title()} three more place is available!")
guest_list.insert(0,'pietro')
guest_list.insert(2,'damiano')
guest_list.append('mehmet')
print(f"You are invite to my dinner {guest_list[0].title()}")
print(f"You are invite to my dinner {guest_list[1].title()}")
print(f"You are invite to my dinner {guest_list[2].title()}")
print(f"You are invite to my dinner {guest_list[3].title()}")
print(f"You are invite to my dinner {guest_list[4].title()}")
print(f"You are invite to my dinner {guest_list[5].title()}")
print(f"You are {len(guest_list)} invit")
print("-------------------------------------------------------------")
print("I can invite only two people for dinner!")
print(f"{guest_list.pop(5).title()} I'm sorry i can't invite you.")
print(f"{guest_list.pop(4).title()} I'm sorry i can't invite you.")
print(f"{guest_list.pop(3).title()} I'm sorry i can't invite you.")
print(f"{guest_list.pop(2).title()} I'm sorry i can't invite you.")
print("-------------------------------------------------------------")
print(f"Hello {guest_list[0].title()}, {guest_list[1].title()} you are still invited.")
print(f"You are {len(guest_list)} invit")
print("-------------------------------------------------------------")
del guest_list[1]
del guest_list[0]
print(f"{guest_list}")
print(f"You are {len(guest_list)} invit")

