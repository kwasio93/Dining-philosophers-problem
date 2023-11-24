import random 
import numpy as nup
import threading
import time

class Philosopher:
    def __init__(self, name, place, current_table_state):
        self.name=name
        self.place=place
        self.hunger_state=100
        self.alive=1
        self.left_hand=0
        self.right_hand=0
        self.Prop=0
        self.Thinks=0
        self.Eats=0
    def Pick_left(self,current_table_state):
        if self.left_hand==0:
            if current_table_state[self.place]==1:
                self.left_hand=1
                current_table_state[self.place]=0
            else:
                self.left_hand=0
        else:
            self.left_hand=self.left_hand
            current_table_state[self.place]=0
    def Pick_right(self,current_table_state):
        if self.right_hand==0:
            if self.place==4:
                if current_table_state[0]==1:
                    self.right_hand=1
                    current_table_state[0]=0
                else:
                    self.right_hand=0
            elif current_table_state[self.place+1]==1:
                self.right_hand=1
                current_table_state[self.place+1]=0
            else:
                self.right_hand=0
        else:
            if self.place==4:
                self.right_hand=self.right_hand
                current_table_state[0]=0
            else:
                self.right_hand=self.right_hand
                current_table_state[self.place+1]=0                
    def Put_left(self,current_table_state):
        if self.left_hand==1:
            self.left_hand=0
            current_table_state[self.place]=1
         
    def Put_right(self,current_table_state):
        if self.right_hand==1:
            if self.place==4:
                self.right_hand=0
                current_table_state[0]=1
            else:
                self.right_hand=0
                current_table_state[self.place+1]=1
                
    def Evolution(self):
        if self.alive==1:
            self.hunger_state+=-5
        else:
            print(self.name+" died!")
    def Think(self):
        if self.alive==1:  
            self.hunger_state=self.hunger_state
        else:
            print(self.name+" died!")
    def Eat(self):
        if self.alive==1:
            self.hunger_state+=15
            if self.hunger_state>100:
                self.hunger_state=100
        else:
            print(self.name+" died!")
    def IsDead(self):
        if self.hunger_state<=0:
            self.alive=0
            
state=[1,1,1,1,1]            

def Activity(state,philo):
    if philo.hunger_state>=50:
        Value=0
    else:
        Value=1
    philo.prop=Value
    if Value==1:
        Eating(philo)
    elif Value==0:
        Thinking(philo)
    # plik.write(str(state[0])+" "+str(state[1])+" "+str(state[2])+" "+str(state[3])+" "+str(state[4])+"\n")

def Eating(Philo):
    print(Philo.name)
    if Philo.alive==1:
        if (Philo.left_hand==0 and Philo.right_hand==0):
            time.sleep(Philo.place/100)
            Philo.Pick_left(state)
            time.sleep((4-Philo.place)/50)
            if Philo.left_hand==1:
                time.sleep((4-Philo.place)/50)
                if Philo.place!=4:
                    if state[Philo.place+1]!=1:
                        Philo.Put_left(state)
                    else:
                        Philo.Pick_right(state)
                else:
                    if state[0]!=1:
                        Philo.Put_left(state)
                    else:
                        Philo.Pick_right(state)
                time.sleep(Philo.place/100)
            else:
                time.sleep(Philo.place/100)
                time.sleep((4-Philo.place)/100)
        
        # if Philo.left_hand==1:
        #     time.sleep((4-Philo.place)/1000)
        #     Philo.Pick_right(state)
        #     if Philo.right_hand==0:
        #         Philo.Put_left(state)
        #         print(Philo.name,Philo.left_hand,i)
        #     time.sleep(Philo.place/1000)
        if (Philo.left_hand==1 and Philo.right_hand==1):
            Philo.Eat()
            Philo.Thinks=0
            Philo.Eats=1
        else:
            Philo.Think()
            Philo.Thinks=-1
            Philo.Eats=0
        if Philo.left_hand==1 and state[Philo.place]==1:
            print(Philo.name)
    else:
        Philo.Thinks=-1
        Philo.Eats=-1
        time.sleep(Philo.place/100)
        time.sleep((4-Philo.place)/100)        
        time.sleep(Philo.place/100)
        time.sleep((4-Philo.place)/100)
def Thinking(Philo):
    print(Philo.name)
    if Philo.alive==1:
        Philo.Put_right(state)
        Philo.Put_left(state)
        Philo.Think()
        Philo.Thinks=1
        Philo.Eats=0
        time.sleep(Philo.place/100)
        time.sleep((4-Philo.place)/100)
        time.sleep(Philo.place/100)
        time.sleep((4-Philo.place)/100)
    else:
        Philo.Thinks=-1
        Philo.Eats=-1
        time.sleep(Philo.place/100)
        time.sleep((4-Philo.place)/100)
        time.sleep(Philo.place/100)
        time.sleep((4-Philo.place)/100)
# def problem(philo):
#     plik=open(philo.name+".txt",'w')
#     plik2=open(philo.name+"_Values.txt",'w')
#     plik3=open(philo.name+"state.txt","w")

#     for i in range(0,100):
#         philo.Evolution()
#         Activity(philo.hunger_state,philo,i)
#         philo.IsDead()
#         plik.write(str(philo.alive)+"\n")
#         plik.write(str(philo.hunger_state)+"\n")
#         plik.write("#######################"+str(i))
#         if philo.place!=4:
#             plik2.write("Left hand: "+str(philo.left_hand)+" Right hand: "+str(philo.right_hand)+" Left side: "+str(state[philo.place])+" Right side: "+str(state[philo.place+1])+" Thinks: "+str(philo.Thinks)+" Eats: "+str(philo.Eats)+" hunger: "+str(philo.hunger_state)+"\n")
#             plik2.write("######################"+str(i)+" \n")
#         else:
#             plik2.write("Left hand: "+str(philo.left_hand)+" Right hand: "+str(philo.right_hand)+" Left side: "+str(state[philo.place])+" Right side: "+str(state[0])+" Thinks: "+str(philo.Thinks)+" Eats: "+str(philo.Eats)+" hunger: "+str(philo.hunger_state)+"\n")      
#             plik2.write("######################"+str(i)+" \n")
#         plik3.write(str(state[0])+" "+str(state[1])+" "+str(state[2])+" "+str(state[3])+" "+str(state[4])+"\n")
#         time.sleep(1/2)
#     plik.close()
#     plik2.close()
#     plik3.close()
plik0=open("Arystoteles.txt","w")
plik0.close()
plik1=open("Kant.txt","w")
plik1.close()
plik2=open("Kartezjusz.txt","w")
plik2.close()
plik3=open("Platon.txt","w")
plik3.close()
plik4=open("Sokrates.txt","w")
plik4.close()
num=[0,0,0,0,0]
def problem(philo):
    num[philo.place]+=1
    plik=open(philo.name+".txt","a")
    philo.Evolution()
    Activity(philo.hunger_state,philo)
    philo.IsDead()
    print(philo.name,philo.hunger_state,num[philo.place])
    if philo.place!=4:
        plik.write(str(num[philo.place])+" "+"Left hand: "+str(philo.left_hand)+" Right hand: "+str(philo.right_hand)+" Left side: "+str(state[philo.place])+" Right side: "+str(state[philo.place+1])+" Thinks: "+str(philo.Thinks)+" Eats: "+str(philo.Eats)+" hunger: "+str(philo.hunger_state)+"\n")    
    else:
        plik.write(str(num[philo.place])+" "+"Left hand: "+str(philo.left_hand)+" Right hand: "+str(philo.right_hand)+" Left side: "+str(state[philo.place])+" Right side: "+str(state[0])+" Thinks: "+str(philo.Thinks)+" Eats: "+str(philo.Eats)+" hunger: "+str(philo.hunger_state)+"\n")    
    plik.close()
        

Arystoteles=Philosopher("Arystoteles",0,state)
Platon=Philosopher("Kant",1,state)
Kant=Philosopher("Kartezjusz",2,state)
Sokrates=Philosopher("Platon",3,state)
Kartezjusz=Philosopher("Sokrates",4,state)


philo_names=[Arystoteles, Platon, Kant, Sokrates, Kartezjusz]
def funkcja():
    Philos=[
            threading.Thread(target = problem,args=(philo,))
            for philo in philo_names
            ]
    
    for phil in Philos:
        phil.start()
    for phil in Philos:
        phil.join()

print("Koniec")


for i in range(0,100):
    funkcja()