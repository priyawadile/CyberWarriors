# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
#init python:
    #import subprocess
    #import webbrowser



screen redButton():
    imagebutton:
        xalign 0.5
        yalign 0.5
        auto "red_button_%s.png" action [ToggleScreen("redButton"), Jump("certform")]

define e = Character("Eileen", color="#FF0044")
define s = Character("Sylvie blue", color = "#009dff")
define g = Character("Sylvie green", color = "#008000")
define l = Character("Lucy", color = "#A020F0")
define pov = Character("[povname]")
image desktop = "desktop page.png"
image mail = "mail page.png"
$ safe = True
# The game starts here.

label certform:
    $ renpy.run(OpenURL('https://forms.gle/DiWt2bjSZSB3Kafp6'))
    $ renpy.quit()
    
    

label start:
    show bg lecturehall
    show eileen vhappy at left          

    # Character introduction
    $ povname = renpy.input("What is your name?", length = 32)
    $ povname = povname.strip()
    
    e "Hii [povname]! Hope you are doing well."

    e "Welcome to Cybersecurity Warrior!"

    e "Are you brave enough to become a CYBERSECURITY WARRIOR??"
    menu:
        "Yes":
            "That's the spirit!! Lets go then.."
        "No":
            "Oh don't be scared, you can do this!"

    e "This game will take you through few cybercrime challenges where you should smartly tackle and handle the hacker to become the winner!"
    e "Let's start with Level 1 of quiz"
    e "All the best"

    hide eileen with dissolve

    show lucy happy at left
    l "Hello, I am the cybersecurity examiner."
    l "Today, I'll test your knowledge on cybersecurity."
    l "Are you ready for the quiz?"

    menu:
        "Yes":
            jump quiz_start
        "No":
            "Alright, take your time. Let me know when you're ready."

    # Label to start the quiz
    label quiz_start:
        $score = 0  # Initialize the score variable

        l "Great! Let's begin."
        l "Cybersecurity: Protecting Digital Assets"

        "Amy is a high school student who loves spending time online, chatting with friends, playing games, and doing research for school projects." 
        "One day, while browsing the internet, she comes across a website claiming to offer free downloads of popular games and apps."
        "Excited about the prospect of getting new games without paying, Amy clicks on the download button and installs the software on her computer."
        "However, shortly after installing the software, Amy notices that her computer starts behaving strangely. Pop-up ads appear frequently, her computer slows down, and she receives a strange email asking for personal information."
        "Concerned about the security of her computer and her online accounts, Amy seeks advice on how to stay safe online."

        # Ask the first question
        jump question1

    label question1:
        "What activity was Amy engaged in when she encountered the cybersecurity issue?"

        menu:
            "a) Playing outdoor games":
                "Incorrect."
                jump question1
            "b) Browsing the internet":
                $score += 1
                "Correct! You may proceed to the next question."
                jump question2
            "c) Reading a book":
                "Incorrect."
                jump question1
            "d) Watching TV":
                "Incorrect."
                jump question1

    label question2:
        if score >= 1:
            "You can proceed to the next question."
            "What is the purpose of pop-up ads on websites?"

            menu:
                "a) To provide useful information to users":
                    "Incorrect. It will hack our data."
                    jump question2
                "b) To increase internet speed":
                    "Incorrect. It will lower your speed of internet."
                    jump question2
                "c) To generate revenue for website owners":
                    $score += 1
                    "Correct! You may proceed to the next question."
                    jump question3
                "d) To enhance the browsing experience":
                    "Incorrect. It decreases your experience of browsing."
                    jump question2
        else:
            "You need to answer the previous question correctly before moving on."
  
    label question3:
        if score >= 2:
            "You can proceed to the next question."
            "What changes did Amy notice on her computer after installing the software?"

            menu:
                "a) Nothing unusual":
                    "Incorrect."
                    jump question3
                "b) Faster performance and fewer ads":
                    "Incorrect."
                    jump question3
                "c) Strange behavior, frequent pop-up ads, and slower performance":
                    $score += 1
                    "Correct! You may proceed to the next question."
                    jump question4
                "d) Improved security features":
                    "Incorrect."
                    jump question3
        else:
            "You need to answer the previous question correctly before moving on."
 
    label question4:
        if score >= 3:
            "You can proceed to the next question."
            "How can Amy protect her computer and online accounts from cyber threats?"

            menu:
                "a) Share her passwords with friends for safekeeping":
                    "Incorrect. It will lead to more chances of hacking."
                    jump question4
                "b) Install antivirus software and keep it updated":
                    $score += 1
                    "Correct! You may proceed to the next question."
                    jump question5
                "c)Click on random links and pop-up ads":
                    "Incorrect. It will lead to harm to the system as well."
                    jump question4
                "d) Post personal information on social media":
                    "Incorrect. It is not an appropriate way at all"
                    jump question4
        else:
            "You need to answer the previous question correctly before moving on."


    label question5:
        if score >= 4:
            "You can proceed to the next question."
            "What did Amy find on the website that she clicked on?"

            menu:
                "a) Free tutorials for school projects":
                    "Incorrect. Encryption is not related to browsing speed."
                    jump question5
                "b) Online quizzes for entertainment":
                    "Incorrect. Encryption is not related to social media followers."
                    jump question5
                "c) Virtual tours of famous museums":
                    "Incorrect. Encryption is not involved in password generation."
                    jump question5
                "d) Free downloads of popular games and apps":
                    $score += 1
                    "Correct! You have completed the quiz."
                    jump end


                    
        else:
            "You need to answer the previous questions correctly before moving on."

    label end:
        "Thank you for participating in the cybersecurity quiz. Goodbye!"
        
    #$answer == False
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene desktop page 2

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy
    
    

    # These display lines of dialogue.

    e "Hellooo... I'm back!"

    e "So [povname]... I heard you have successfully completed Level 1."

    e "Congrats [povname]!!!"

    show eileen vhappy at left with move
    show sylvie blue smile at right
    s "Hey Hey... What are you doing?"

    e "Hey! We were talking about cybersecurity."

    e "So you have the knowledge but can you apply it in your real life?"
    
    hide sylvie blue with dissolve
    show eileen concerned at right with move

    menu :
        
        "Yes, I'm confident about Cybersecurity.":
            pass
        "Yes, but I need more practice.":
            pass
        
    show sylvie blue giggle at left with move
    show eileen vhappy at right
    s "Oh well, I'm sure you can. "

    s "So let's start with next level."

    label start_level2:

        scene desktop 

        show sylvie blue surprised at right with move
        hide eileen with dissolve
        s "Looks like you have recieved a mail."

        s "Let's open it!"

        hide sylvie blue with dissolve

        scene mail

        show eileen vhappy at right

        e "The mail says, you have won the contest!"
        e "Woahh! Congratssss"

        show eileen concerned at right
        e "What do you think should we do?"

        menu:
            "Should we move forward and open the link to avail the prize?"

            "Yess, let's do it.":
                $ safe = False

            "No, it doesn't seem right":
                $ safe = True
    
        if safe:
            jump correctpath
        else:
            jump openlink

        label openlink:
            hide eileen with dissolve
            menu:
                "Are you sure??"
                "I think...No":
                    $ safe = True
                    

                "Yes, open it":
                    $ safe = False
                    
            
            if safe:
                jump correctpath
            else:
                jump fill_form
            
        label fill_form:
            scene form page
            hide eileen with dissolve
            show sylvie blue surprised at right
            s "It's asking to fill the form..."
            menu:
                "Should we fill it [povname]?"
                "Yessss":
                    $ safe = False
                
                "No...looks suspicious":
                    $ safe = True

            if safe:
                jump correctpath
            else:
                jump otp

        label correctpath:
            hide eileen with dissolve
            show sylvie blue surprised at right
            s "Whyyyy??? It was a great chance for a trip to Disney Land!"

            show eileen happy at left
            e "You did the right thing [povname]."
            e "You shouldn't click on any links given in the email neither should you give out your personal details on these sites. Giving out credit card details will allow then to access it and the otp which you are giving them gives approval that you are the one making transaction, which is not true."
            e "The hacker tries to immitate you and credit themselves a large amount. You should be careful with these type of crime."

            jump nextlevel


        label otp:
            scene otp page
            menu:
                e "Should we give out the OTP?"
                "Yes, why not?":
                    $ safe = False
                    
                "No, doesn't look right":
                    $ safe = True

            if safe:
                jump nextlevel
            else:
                jump lost_level2

        
            
        label lost_level2:
            scene lost lev2
            e "You lose!"
            menu:
                "Try Again?"
                "Yes, will win this time!":
                    jump start_level2
                "No":
                    "Oh no...see you soon"
                    $ renpy.quit()
        
        label nextlevel:
            show sylvie blue giggle at right
            s "Yeah [povname]! You made it to the next level"
            jump start_level3

        label start_level3:
            scene winner
            show eileen vhappy at left
            show sylvie green smile at right
            e "Congratulations and Welcome to the Final Level!"
            g "Pheww....You have done a quite of work"
            e "I'm sure you will enjoy your success at the end"
            e "Keep going!!"

            label start_lev3:
                scene desktop page 2
                show eileen happy at left
                show sylvie green giggle at right
                g "Heyy..have you heard of new popular game??"
                show eileen concerned at left
                e "Yeah, but it isn't free..."
                g "So what, we can download the pirated version"
                e "Don't you know it's unsafe and illegal to download pirated games??!!"
                scene pirated website
                show sylvie green normal at right
                g "Hey relax..it isn't a big deal"
                menu:
                    "What do you think [povname]?"
                    "Let's download for free, nothing happens":
                        $ safe = False
                        
                    "It's not safe and our device can get hacked":
                        $ safe = True
                        

                if safe:
                    jump safechoice
                else:
                    jump download_game

                label download_game:
                    scene download page
                    show sylvie green normal at right
                    show eileen happy at left
                    g "Let's download....don't you worry"
                    e "I'm not sure...but okay"
                    scene danger 1
                    g "Oh no....What's Happening!!!!!"
                    scene danger 2
                    e "I told you it wasn't safe"
                    scene lost lev3 
                    e "You lose [povname]! "
                    menu:
                        "Try Again?"
                        "Yes, will win this time!":
                            jump start_lev3
                        "No":
                            "Oh no...see you soon [povname]"
                            $ renpy.quit()

                

                label safechoice:
                    scene winner
                    show sylvie green giggle at right
                    show eileen vhappy at left
                    e "Great Choice!"
                    g "Yeah! You did it"
                    e "Pirated websites often distribute copyrighted content without permission, which is a violation of intellectual property laws. Engaging in such activities can lead to legal consequences, including fines and potential criminal charges."
                    e "Pirated websites are notorious for hosting malicious software, including viruses, malware, and other forms of cyber threats. Downloading or streaming content from such sites can compromise your device's security and privacy."
                    g "[povname] you are the REAL CYBER WARRIOR"

                    e "Congratulations [povname]!"
                    e "Click on the Red Button to receive the completion certificate"
                    e "You will get it on your email id after filling out the form"
                    e "Thank you for playing!"
                    scene black
                    call screen redButton
                    


                    

                    


                    
                    
                    
    scene desktop




    # This ends the game.

    return