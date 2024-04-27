database;
[
    object defender()
        {
            int HP
            dict cardset
                {
                    card:
                    main:
                    vice:
                }
        }


    object attack1
        {
            dict cardset
        }
        ...
    object attack2
        {
            dict cardset
        }
        ...
    object attack_n
        {
            dict cardset
        }


    dict standard_seqeunce
]




build_tool_cardset_reader(cardset_list);
{
    lod = []

    for i in cardset_list:
        tmpd = {"card": 0, "sequence_main": 0, "sequence_vice": 0}

        tmpd["card"] = i
        tmpd["sequence_main"] = key1[i[1:2]]
        tmpd["sequence_vice"] = key2[i[0:1]]

        lod.append(tmpd)

    return lod
}




build_base();
{
    f = open()

    get HP & rounds
        {
            readline1 ===> list_L1
            HP = list_L1[0]
            rounds = list_L1[1]
        }

    get defender
        {
            readline2 ===> list_L2  //cardset
            defender[cardset] = reader(list_L2)
            defender[HP] = list_L1[0]
        }

    get attack_n
        {
            list attacks = []
            loop for restLine in rest_readline
                {
                     append(reader:restLine)
                } 

            
        }
}




workflow;
[
    round = 1

    loop("HP > 0","len(defender_cardset) > 0")
        {
            check winner

            cardset_attack_input

            check_cardset_format

            searching_overcard_in_defender_cardset_in_corresponding_format

            copy_closest_overcard_into_list_repulse
    
            print_the_smallest_one

            delete_the corresponding item in defender_cardset

            round += 1
        }
]




cardset_attack_input();
{
    attack1 = attacks[i - 1]
}




check_cardset_format();
{
    int format = len(attack1)
}




searching_overcard_in_defender_cardset_in_corresponding_format();
{
    list_tmp = []
    for x in defender[cardset] :
        if x["sequence_main"] > attack1[0]["sequence_main"]:
            {
                list_tmp.append(x)
            }

        elif x["sequence_main"] == attack1[0]["sequence_main"] and x["sequence_vice"] > attack1[0]["sequence_vice"]:
        {
                list_tmp.append(x)
        }

        elsi
        {
            pass
        }
}




copy_overcard_into_list_repulse();
{
    list_repulse = list_tmp[-format:]
}




print_the_smallest_one();
{
    print list_repulse
}




delete_the_corresponding_item_in_defender_cardset();
{
    del defender[cardset][len(list_tmp) - 1 - format: len(list_tmp) - 1]
}






test_input_here:

1, 2, 3, 4, 5\n, 6, 7, 8, 9, 10


5 , 3
SA , CA , DK , SJ , CJ , ST , HT , H5 , H3 , S3 , C3
S2 , H2
D2
D3
HA , DA
SQ , DQ


0   1   2   3  4  5  6  7  8  9  10 11 12 13 14

-12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1

1   2   3   4  5  6  7  8  9  10 11 12 13 14 15 

format = 2


 defender["HP"] > 0 and len(defender["cardset"]) > 0
