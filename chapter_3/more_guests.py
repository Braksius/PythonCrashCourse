guest_list = ['manuela','stefania','angelo']
print(f"You are invite to my dinner {guest_list[0].title()}")
print(f"You are invite to my dinner {guest_list[1].title()}")
print(f"You are invite to my dinner {guest_list[2].title()}")
print(f"Hello {guest_list[0].title()}, {guest_list[1].title()}, {guest_list[2].title()} you are invited!")
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

