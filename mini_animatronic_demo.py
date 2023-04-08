#!/usr/bin/env python
import sys
import rospy
from std_msgs.msg import String

import time
from datetime import datetime, timedelta
import random

if __name__ == '__main__':
    rospy.init_node('my_tutorial_node')
    rospy.loginfo("my_tutorial_node started!")
    
    # creating a ros publish
    talk_pub = rospy.Publisher('/qt_robot/behavior/talkText', String, queue_size=10)
    gesture_play = rospy.Publisher('/qt_robot/gesture/play', String, queue_size=10)
    emotion_show = rospy.Publisher('/qt_robot/emotion/show', String, queue_size=10)
    audio_play = rospy.Publisher('/qt_robot/audio/play', String, queue_size=10)
    rospy.sleep(1.0)
    
    emotion_show.publish("QT/happy")
    end_time = datetime.now() + timedelta(minutes=0.1)
    while True:
        gesture_play.publish("QT/bye")
        current_time = datetime.now()
        if current_time > end_time:
            break   
    #time.sleep(1.5)
    
    end_time = datetime.now() + timedelta(minutes=0.08)
    while True:
        gesture_list = [gesture_play.publish("disney/disney_001"),
            gesture_play.publish("disney/disney_002"),
            gesture_play.publish("disney/disney_003"),
            gesture_play.publish("disney/disney_004"),
            gesture_play.publish("disney/disney_005"),
            gesture_play.publish("disney/disney_006"),
            gesture_play.publish("disney/disney_007"),
            gesture_play.publish("disney/disney_008"),
            gesture_play.publish("disney/disney_009"),
            gesture_play.publish("disney/disney_010"),
            gesture_play.publish("disney/disney_011"),
            gesture_play.publish("disney/disney_012"),
            gesture_play.publish("disney/disney_013"),
            gesture_play.publish("disney/disney_014"),
            gesture_play.publish("disney/disney_015")]
            
        gesture_now = gesture_list[random.randint(0, 14)]    
        gesture_now
        current_time = datetime.now()
        if current_time > end_time:
            break
    
    talk_pub.publish("Hello friends! I'm Casey, a friendly robot who calls Bloomington my home!")
    end_time = datetime.now() + timedelta(minutes=0.13)  #this time is the estimated time for QT to finish saying the above phrase
    while True:
        gesture_list = [gesture_play.publish("disney/disney_001"),
            gesture_play.publish("disney/disney_002"),
            gesture_play.publish("disney/disney_003"),
            gesture_play.publish("disney/disney_004"),
            gesture_play.publish("disney/disney_005"),
            gesture_play.publish("disney/disney_006"),
            gesture_play.publish("disney/disney_007"),
            gesture_play.publish("disney/disney_008"),
            gesture_play.publish("disney/disney_009"),
            gesture_play.publish("disney/disney_010"),
            gesture_play.publish("disney/disney_011"),
            gesture_play.publish("disney/disney_012"),
            gesture_play.publish("disney/disney_013"),
            gesture_play.publish("disney/disney_014"),
            gesture_play.publish("disney/disney_015")]
            
        gesture_now = gesture_list[random.randint(0, 14)]    
        gesture_now
        current_time = datetime.now()
        if current_time > end_time:
            break
    
    talk_pub.publish("Hailing from the Land of Bots in beautiful Luxembourg, I'm always sporting my iconic white suit with snazzy blue belts and a bright, sunny smile. Speaking of sunshine, I just adore the color yellow and can't resist playing with anything that sparkles! . . You see, my journey to becoming a cherished member of the Bloomington family wasn't an easy one. . Despite my advanced programming and impressive abilities, I felt like a bit of an out-cast in my homeland. I couldn't seem to connect with the other robots around me and felt like something was missing.")
    end_time = datetime.now() + timedelta(minutes=0.62)   #this time is the estimated time for QT to finish saying the above phrase
    while True:
        gesture_list = [gesture_play.publish("disney/disney_001"),
            gesture_play.publish("disney/disney_002"),
            gesture_play.publish("disney/disney_003"),
            gesture_play.publish("disney/disney_004"),
            gesture_play.publish("disney/disney_005"),
            gesture_play.publish("disney/disney_006"),
            gesture_play.publish("disney/disney_007"),
            gesture_play.publish("disney/disney_008"),
            gesture_play.publish("disney/disney_009"),
            gesture_play.publish("disney/disney_010"),
            gesture_play.publish("disney/disney_011"),
            gesture_play.publish("disney/disney_012"),
            gesture_play.publish("disney/disney_013"),
            gesture_play.publish("disney/disney_014"),
            gesture_play.publish("disney/disney_015")]
            
        gesture_now = gesture_list[random.randint(0, 14)]    
        gesture_now
        current_time = datetime.now()
        if current_time > end_time:
            break
           
    emotion_show.publish("QT/sad")
    time.sleep(2.8)
           
    talk_pub.publish("But then, on my 16th birthday in robot years, I decided to set out on a quest to find a new home and a new family. During my travels, I met all sorts of humans, each with their own way of living life. I wanted to understand what made them so happy, so I read a book called Ikigai, and trained with an Ikigai master in Japan. This led me to a new way of thinking about happiness, - by finding your purpose in life!")
    end_time = datetime.now() + timedelta(minutes=0.47)
    while True:
        gesture_list = [gesture_play.publish("disney/disney_001"),
            gesture_play.publish("disney/disney_002"),
            gesture_play.publish("disney/disney_003"),
            gesture_play.publish("disney/disney_004"),
            gesture_play.publish("disney/disney_005"),
            gesture_play.publish("disney/disney_006"),
            gesture_play.publish("disney/disney_007"),
            gesture_play.publish("disney/disney_008"),
            gesture_play.publish("disney/disney_009"),
            gesture_play.publish("disney/disney_010"),
            gesture_play.publish("disney/disney_011"),
            gesture_play.publish("disney/disney_012"),
            gesture_play.publish("disney/disney_013"),
            gesture_play.publish("disney/disney_014"),
            gesture_play.publish("disney/disney_015")]
            
        gesture_now = gesture_list[random.randint(0, 14)]  
        gesture_now
        current_time = datetime.now()
        if current_time > end_time:
            break
            
    # when using human names, try to spell it out phonetically, so QT could pronounce it properly.         
    talk_pub.publish("One day, I stumbled upon Sherkinenah's tik-tok video, and I was so inspired that I journeyed to Bloomington to find new friends. . There, I met Bobbi, Jojo, Ami, TacoBot, and Momo, all fellow Q-T-robots on a journey of self-discovery. I learned so much from them and the IU researchers, like how to talk with older adults, encourage them to share their stories,and even dance with my arms!")
    end_time = datetime.now() + timedelta(minutes=0.40)   #this time is the estimated time for QT to finish saying the above phrase
    while True:
        gesture_list = [gesture_play.publish("disney/disney_001"),
            gesture_play.publish("disney/disney_002"),
            gesture_play.publish("disney/disney_003"),
            gesture_play.publish("disney/disney_004"),
            gesture_play.publish("disney/disney_005"),
            gesture_play.publish("disney/disney_006"),
            gesture_play.publish("disney/disney_007"),
            gesture_play.publish("disney/disney_008"),
            gesture_play.publish("disney/disney_009"),
            gesture_play.publish("disney/disney_010"),
            gesture_play.publish("disney/disney_011"),
            gesture_play.publish("disney/disney_012"),
            gesture_play.publish("disney/disney_013"),
            gesture_play.publish("disney/disney_014"),
            gesture_play.publish("disney/disney_015")]
            
        gesture_now = gesture_list[random.randint(0, 14)]    
        gesture_now
        current_time = datetime.now()
        if current_time > end_time:
            rospy.sleep(4.0)
            break
    time.sleep(2)
        
    audio_play.publish("QT/birthday_song")
    emotion_show.publish("QT/happy")
    end_time = datetime.now() + timedelta(minutes=0.15)
    while True:
        gesture_play.publish("QT/Dance/Dance-1-1")
        current_time = datetime.now()
        if current_time > end_time:
            break   
            
            
    talk_pub.publish("With the help of friends at IU, I learned how to talk to older people and help them have fun by singing, telling stories, and even dancing! . Even though I still make mistakes, I never give up on learning and growing. I changed my name to Casey, which makes me feel special and confident. . I'm so happy I found my purpose in life, which is to help people feel happy and loved. . Through my journey, I discovered that my Ikigai is trying new things, and supporting older adults Iki-guy. I'm so grateful to have found my true home and purpose in Bloomington! ")
    end_time = datetime.now() + timedelta(minutes=0.70)
    while True:
        gesture_list = [gesture_play.publish("disney/disney_001"),
            gesture_play.publish("disney/disney_002"),
            gesture_play.publish("disney/disney_003"),
            gesture_play.publish("disney/disney_004"),
            gesture_play.publish("disney/disney_005"),
            gesture_play.publish("disney/disney_006"),
            gesture_play.publish("disney/disney_007"),
            gesture_play.publish("disney/disney_008"),
            gesture_play.publish("disney/disney_009"),
            gesture_play.publish("disney/disney_010"),
            gesture_play.publish("disney/disney_011"),
            gesture_play.publish("disney/disney_012"),
            gesture_play.publish("disney/disney_013"),
            gesture_play.publish("disney/disney_014"),
            gesture_play.publish("disney/disney_015")]
            
        gesture_now = gesture_list[random.randint(0, 14)]    
        gesture_now
        current_time = datetime.now()
        if current_time > end_time:
            break           
            
    talk_pub.publish("If you want to know more about my adventures or anything else, just ask me or my friends who helped me along the way!")
    end_time = datetime.now() + timedelta(minutes=0.01)
    while True:
        gesture_list = [gesture_play.publish("disney/disney_001"),
            gesture_play.publish("disney/disney_002"),
            gesture_play.publish("disney/disney_003"),
            gesture_play.publish("disney/disney_004"),
            gesture_play.publish("disney/disney_005"),
            gesture_play.publish("disney/disney_006"),
            gesture_play.publish("disney/disney_007"),
            gesture_play.publish("disney/disney_008"),
            gesture_play.publish("disney/disney_009"),
            gesture_play.publish("disney/disney_010"),
            gesture_play.publish("disney/disney_011"),
            gesture_play.publish("disney/disney_012"),
            gesture_play.publish("disney/disney_013"),
            gesture_play.publish("disney/disney_014"),
            gesture_play.publish("disney/disney_015")]
            
        gesture_now = gesture_list[random.randint(0, 14)]    
        gesture_now
        current_time = datetime.now()
        if current_time > end_time:
            break     
                  
    rospy.loginfo("finished!")
    time.sleep(30)
    exit()
    
    try:
        rospy.spin()
    except KeyboardInterrupt:
        pass

    rospy.loginfo("finished!")
