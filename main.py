
import pyttsx3
import speech_recognition as sr


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening')
        pause_threshold = 0.7
        audio = r.listen(source)
        try:
            print("Recognizing")
            Query = r.recognize_google(audio, language='en-in')
            print("the command is printed=", Query)
        except Exception as e:
            print(e)
            print("can you please say again. /can you please say more simple.")
            return "None"
    return Query


def speak(audio):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(audio)
    engine.runAndWait()


def Hello():
    speak("hello sir hello, how can i help you. / hello, need information about astronomy?")


def Take_query():
    while(True):
        query = takeCommand().lower()
        if "hello" in query or "introduce yourself" in query:
            speak("hello to the principal, to the vice principal, to the superintendent, to the school's officials and employees, to the teachers and all the students. My name is zak, I am an assistant of astronomy supject, i can help you learn alot about astronomy subject ")

        elif "what can you do" in query:
            speak("i can tell you some information about astronomy, this machine also contain telescope for you to research about the space")
        elif "how are you" in query:
            speak("I'm fine. I'm really fine. I'm about to help you anything you can imagine about astronomy. Don't worry about you don't know anything")
        elif "where is the earth" in query:
            speak("Earth is located in one of the spiral arms of the Milky Way (called the Orion Arm) which lies about two-thirds of the way out from the center of the Galaxy. Here we are part of the Solar System - a group of eight planets, as well as numerous comets and asteroids and dwarf planets which orbit the Sun.")
        elif "where is the mars" in query:
            speak("Mars is the fourth planet from the Sun and the second-smallest planet in the Solar System, being larger than only Mercury. ")
        elif "where is the mercury" in query:
            speak("Earth is located in one of the spiral arms of the Milky Way (called the Orion Arm) which lies about two-thirds of the way out from the center of the Galaxy. Here we are part of the Solar System - a group of eight planets, as well as numerous comets and asteroids and dwarf planets which orbit the Sun.")
        elif "where is the venus" in query:
            speak("Earth is located in one of the spiral arms of the Milky Way (called the Orion Arm) which lies about two-thirds of the way out from the center of the Galaxy. Here we are part of the Solar System - a group of eight planets, as well as numerous comets and asteroids and dwarf planets which orbit the Sun.")
        elif "where is the jupiter" in query:
            speak("Jupiter is the fifth planet from the Sun and the largest in the Solar System.")
        elif "where is the saturn" in query:
            speak("Saturn is the sixth planet from the Sun and the second-largest in the Solar System, after Jupiter.")
        elif "where is the uranus" in query:
            speak("Uranus is the seventh planet from the Sun. Its name is a reference to the Greek god of the sky, Uranus, who, according to Greek mythology, was the great-grandfather of Ares, grandfather of Zeus and father of Cronus. It has the third-largest planetary radius and fourth-largest planetary mass in the Solar System.")
        elif "where is the neptune" in query:
            speak("Neptune is the eighth planet from the Sun and the farthest known solar planet. In the Solar System, it is the fourth-largest planet by diameter, the third-most-massive planet, and the densest giant planet. It is 17 times the mass of Earth, and slightly more massive than its near-twin Uranus.")
        elif "general information aboyut the solar system" in query:
            speak("The Solar System is the gravitationally bound system of the Sun and the objects that orbit it. It formed 4.6 billion years ago from the gravitational collapse of a giant interstellar molecular cloud. The vast majority (99.86%) of the system's mass is in the Sun, with most of the remaining mass contained in the planet Jupiter. The four inner system planets—Mercury, Venus, Earth and Mars—are terrestrial planets, being composed primarily of rock and metal. The four giant planets of the outer system are substantially larger and more massive than the terrestrials. The two largest, Jupiter and Saturn, are gas giants, being composed mainly of hydrogen and helium; the next two, Uranus and Neptune, are ice giants, being composed mostly of volatile substances with relatively high melting points compared with hydrogen and helium, such as water, ammonia, and methane. All eight planets have nearly circular orbits that lie near the plane of Earth's orbit, called the ecliptic.")
        elif "general information about the universe" in query:
            speak("The universe (Latin: universus) is all of space and time and their contents, including planets, stars, galaxies, and all other forms of matter and energy. The Big Bang theory is the prevailing cosmological description of the development of the universe. According to this theory, space and time emerged together 13.787±0.020 billion years ago, and the universe has been expanding ever since the Big Bang. While the spatial size of the entire universe is unknown, it is possible to measure the size of the observable universe, which is approximately 93 billion light-years in diameter at the present day.")
        elif "famous stars" in query:
            speak("Polaris, Sirius, Alpha Centauri System, Betelgeuse, etcetera")
        elif "polaris star information" in query:
            speak("Polaris is a star in the northern circumpolar constellation of Ursa Minor. It is designated α Ursae Minoris (Latinized to Alpha Ursae Minoris) and is commonly called the North Star or Pole Star. With an apparent magnitude that fluctuates around 1.98,[3] it is the brightest star in the constellation and is readily visible to the naked eye at night.[16] The position of the star lies less than 1° away from the north celestial pole, making it the current northern pole star. The stable position of the star in the Northern Sky makes it useful for navigation.")
        elif "Polaris Australis general information" in query:
            speak("Polaris Australis (Sigma Octantis) is the closest naked-eye star to the south celestial pole, but at apparent magnitude 5.47 it is barely visible on a clear night, making it unusable for navigational purposes. It is a yellow giant 294 light years from Earth.")
        elif "general information about Stephenson 2-18" in query:
            speak("Stephenson 2-18 (abbreviated to St2-18), also known as Stephenson 2 DFK 1 or RSGC2-18, is a red supergiant (RSG) or possible extreme red hypergiant (RHG) star in the constellation of Scutum. It lies near the open cluster Stephenson 2, which is located about 5.8 kiloparsecs (19,000 light-years) away from Earth in the Scutum–Centaurus Arm of the Milky Way galaxy, and is assumed to be one of a group of stars at a similar distance, although some sources consider it to be an unrelated red supergiant.[5][6] It is among the largest known stars, one of the most luminous red supergiants, and one of the most luminous stars in the Milky Way.")
        elif "bye" in query:
            speak("Good Bye. If you wanna get more information about me and astronomy, just turn me on.")
            exit()

Hello()
Take_query()
