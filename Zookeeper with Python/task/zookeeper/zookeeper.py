def display_habitat(habitat_number):
    habitats = {
    "0": r"""
    Switching on the camera in the camel habitat...
     ___.-''''-.
    /___  @    |
    ',,,,.     |         _.'''''''._
         '     |        /           \
         |     \    _.-'             \
         |      '.-'                  '-.
         |                               ',
         |                                '',
          ',,-,                           ':;
               ',,| ;,,                 ,' ;;
                  ! ; !'',,,',',,,,'!  ;   ;:
                 : ;  ! !       ! ! ;  ;   :;
                 ; ;   ! !      ! !  ; ;   ;,
                ; ;    ! !     ! !   ; ;
                ; ;    ! !    ! !     ; ;
               ;,,      !,!   !,!     ;,;
               /_I      L_I   L_I     /_I
    Look at that! Our little camel is sunbathing!""",

    "1": r"""
    Switching on the camera in the lion habitat...
                                                   ,w.
                                                 ,YWMMw  ,M  ,
                            _.---.._   __..---._.'MMMMMw,wMWmW,
                       _.-""        '''           YP"WMMMMMMMMMb,
                    .-' __.'                   .'     MMMMW^WMMMM;
        _,        .'.-'"; `,       /`     .--""      :MMM[==MWMW^;
     ,mM^"     ,-'.'   /   ;      ;      /   ,       MMMMb_wMW"  @\
    ,MM:.    .'.-'   .'     ;     `\    ;     `,     MMMMMMMW `"=./`-,
    WMMm__,-'.'     /      _.\      F'''-+,,   ;_,_.dMMMMMMMM[,_ / `=_}
    "^MP__.-'    ,-' _.--""   `-,   ;       \  ; ;MMMMMMMMMMW^``; __|
               /   .'            ; ;         )  )`{  \ `"^W^`,   \  :
              /  .'             /  (       .'  /     Ww._     `.  `"
             /  Y,              `,  `-,=,_{   ;      MMMP`""-,  `-._.-,
            (--, )                `,_ / `) \/"")      ^"      `-, -;"\:
    The lion is roaring!""",

    "2": r"""
    Switching on the camera in the deer habitat...
       /|       |\
    `__\\       //__'
       ||      ||
     \__`\     |'__/
       `_\\   //_'
       _.,:---;,._
       \_:     :_/
         |@. .@|
         |     |
         ,\.-./ \
         ;;`-'   `---__________-----.-.
         ;;;                         \_\
         ';;;                         |
          ;    |                      ;
           \   \     \        |      /
            \_, \    /        \     |\
              |';|  |,,,,,,,,/ \    \ \_
              |  |  |           \   /   |
              \  \  |           |  / \  |
               | || |           | |   | |
               | || |           | |   | |
               | || |           | |   | |
               |_||_|           |_|   |_|
              /_//_/           /_/   /_/
    Our 'Bambi' looks hungry. Let's go to feed it!""",

    "3": r"""
    Switching on the camera in the goose habitat...

                                        _
                                    ,-"" "".
                                  ,'  ____  `.
                                ,'  ,'    `.  `._
       (`.         _..--.._   ,'  ,'        \    \
      (`-.\    .-""        ""'   /          (  d _b
     (`._  `-"" ,._             (            `-(   \
     <_  `     (  <`<            \              `-._\
      <`-       (__< <           :
       (__        (_<_<          ;
        `------------------------------------------
    The goose is staring intently at you... Maybe it's time to change the channel?""",

    "4": r"""
    Switching on the camera in the bat habitat...
    _________________               _________________
     ~-.              \  |\___/|  /              .-~
         ~-.           \ / o o \ /           .-~
            >           \\  W  //           <
           /             /~---~\             \
          /_            |       |            _\
             ~-.        |       |        .-~
                ;        \     /        i
               /___      /\   /\      ___\
                    ~-. /  \_/  \ .-~
                       V         V
    This bat looks like it's doing fine.""",

    "5": r"""
    Switching on the camera in the rabbit habitat...
             ,
            /|      __
           / |   ,-~ /
          Y :|  //  /
          | jj /( .^
          >-"~"-v"
         /       Y
        jo  o    |
       ( ~T~     j
        >._-' _./
       /   "~"  |
      Y     _,  |
     /| ;-"~ _  l
    / l/ ,-"~    \
    \//\/      .- \
     Y        /    Y
     l       I     !
     ]\      _\    /"\
    (" ~----( ~   Y.  )
    It looks like we will soon have more rabbits!"""
    }
    print(habitats.get(habitat_number, "Habitat not found!"))
def main():
    while True:
        user_input = input("Please enter the number of the habitat you would like to view or 'exit' to quit: ")
        if user_input == "exit":
            print("See you later!")
            break
        display_habitat(user_input)

if __name__ == "__main__":
    main()