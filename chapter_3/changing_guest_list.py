guest_list = ['manuela','stefania','angelo']
print(f"You are invite to my dinner {guest_list[0].title()}")
print(f"You are invite to my dinner {guest_list[1].title()}")
print(f"You are invite to my dinner {guest_list[2].title()}")
print(guest_list)
print("-------------------------------------------------------------")
guest_revok = 'stefania'
guest_list.remove(guest_revok)
guest_list.append('fabio')
print(f"The guest {guest_revok.title()} are revok your invitation!")
print("-------------------------------------------------------------")
print(f"The new guest list is {guest_list}")
print(f"You are invite to my dinner {guest_list[0].title()}")
print(f"You are invite to my dinner {guest_list[1].title()}")
print(f"You are invite to my dinner {guest_list[2].title()}")
