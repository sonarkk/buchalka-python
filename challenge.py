spell = "-"
while spell != "0":
    if spell in "123456789":
        print ("You chose {}".format(spell))
    else:
        print("Please select a spell to cast: ")
        print("1:\tBlizzaga")
        print("2:\tFiraga")
        print("3:\tWaterga")
        print("4:\tThundaga")
        print("5:\tTornado")
        print("6:\tMeteor")
        print("7:\tUltima")
        print("8:\tFlare")
        print("9:\tFlood")
        print("0:\tCancel")

    spell = input()

