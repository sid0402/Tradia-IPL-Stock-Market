import tkinter as tk 
from tkinter import ttk 
import pandas as pd
from PIL import Image, ImageTk

LARGEFONT = ("Verdana", 35) 
inputs = ('Helvetica', 15)

game_data = pd.read_excel('/Users/siddhantagarwal/Desktop/gamedata.xlsx')
print(game_data, game_data.columns)
game_data.set_index('IPL Players',inplace=True)

your_order = {'Player':[],'Type':[],'Volume':[],'Price':[]}


user_data = {'Player':['Player 1'],'Volume':[1]}

limit = 5000

class tkinterApp(tk.Tk): 
     
    def __init__(self, *args, **kwargs): 
        
        # __init__ function for class Tk 
        tk.Tk.__init__(self, *args, **kwargs) 
        
        container = tk.Frame(self) 
        container.pack(side = "top", fill = "both", expand = True) 

        container.grid_rowconfigure(0, weight = 1) 
        container.grid_columnconfigure(0, weight = 1) 
 
        self.frames = {} 

        for F in (StartPage, PlaceOrder, GameData, YourOrders, UserData, DataChange): 

            frame = F(container, self) 

            self.frames[F] = frame 

            frame.grid(row = 0, column = 0, sticky ="nsew") 

        self.show_frame(StartPage) 

    def show_frame(self, cont): 
        frame = self.frames[cont] 
        frame.tkraise() 

################# STARTPAGE ##################
class StartPage(tk.Frame): 
    def __init__(self, parent, controller): 
        tk.Frame.__init__(self, parent) 
        
        col = 0
        
        '''
        img = tk.PhotoImage(file="/Users/siddhantagarwal/Desktop/tradia.png")
        label = tk.Label(self,image=img)
        label.place(x = 0, y = 0,relheight=1,relwidth=1)

        load = Image.open("/Users/siddhantagarwal/Desktop/tradia.jpg")
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        img.image = render
        img.place(x=200, y=100,height=20,width=250)
        
        '''

        self['bg'] = 'blue'
        
        label = tk.Label(self, text ="Welcome to the Tradia IPL auction simulation!", font = ("Verdana", 20))
        label.config(bg='blue')
        label.grid(row = 0, column = col, padx = 10, pady = 10) 
    
        label = tk.Label(self,bg='blue', text ="To place an order, select PlaceOrder", font = ("Verdana", 15)) 
        label.grid(row = 2, column = 0, padx = 10, pady = 10) 
        label = tk.Label(self, bg='blue',text ="To place an order, select Place Order", font = ("Verdana", 15)) 
        label.grid(row = 3, column = 0, padx = 10, pady = 10) 
        label = tk.Label(self,bg='blue', text ="Game Data, Your Orders and User Data give you more information about the game", font = ("Verdana", 15)) 
        label.grid(row = 4, column = 0, padx = 10, pady = 10) 
        
        button1 = ttk.Button(self, text ="Place Order", 
        command = lambda : controller.show_frame(PlaceOrder)) 
    
        button1.grid(row = 7, column = col, padx = 10, pady = 10) 

        button2 = ttk.Button(self, text ="Game Data", 
        command = lambda : controller.show_frame(GameData)) 
        button2.grid(row = 8, column = col, padx = 10, pady = 10) 

        button3 = ttk.Button(self, text ="Your Orders", 
        command = lambda : controller.show_frame(YourOrders)) 
        button3.grid(row = 9, column = col, padx = 10, pady = 10) 
        
        button4 = ttk.Button(self, text ="User Data", 
        command = lambda : controller.show_frame(UserData)) 
        button4.grid(row = 10, column = col, padx = 10, pady = 10) 
        
        button5 = ttk.Button(self, text ="Data Change", 
        command = lambda : controller.show_frame(DataChange)) 
        button5.grid(row = 11, column = col, padx = 10, pady = 10) 

################### PLACEORDER PAGE############## 
class PlaceOrder(tk.Frame): 
    
    def __init__(self, parent, controller): 
        
        ####### DESIGN #############
        tk.Frame.__init__(self, parent) 
        label = ttk.Label(self, text ="PlaceOrder", font = LARGEFONT) 
        label.grid(row = 0, column = 4, padx = 10, pady = 10) 

        button1 = ttk.Button(self, text ="StartPage", 
                            command = lambda : controller.show_frame(StartPage)) 

        button1.grid(row = 1, column = 0, padx = 5, pady = 5) 
        
        global ipl_player,order_type,order_price

        for i in range(100):   
            label = ttk.Label(self, text ="IPL PLAYER", font = inputs)
            label.grid(row = 2, column = 0, padx = 10, pady = 10)
            ipl_player = ttk.Combobox(self)
            ipl_player['values'] = ['Player '+str(i+1) for i in range(len(game_data.index))]
            ipl_player.grid(row=2,column=1,padx=10,pady=10)
            
            label = ttk.Label(self, text ="ORDER TYPE", font = inputs) 
            label.grid(row = 3, column = 0, padx = 10, pady = 10) 
            #order_type = tk.Entry(self)
            #order_type.grid(row = 3,column = 1, padx = 10, pady = 10)
            order_type = ttk.Combobox(self)
            order_type['values'] = ['Buy','Sell']
            order_type.grid(row = 3, column = 1, padx = 10, pady = 10)
            
            label = ttk.Label(self, text ="ORDER PRICE", font = inputs) 
            label.grid(row = 4, column = 0, padx = 10, pady = 10) 
            order_price = tk.Entry(self)
            order_price.grid(row = 4,column = 1, padx = 10, pady = 10)
            
            def volume_drop():
                
                #player_button.destroy()
                
                global order_volume
                label = ttk.Label(self, text ="ORDER VOLUME", font = inputs) 
                label.grid(row = 5, column = 0, padx = 10, pady = 10)
                order_volume = ttk.Combobox(self)
                
                valid_player = ipl_player.get()
                lim_volume = game_data.at[valid_player,'Volume']
                valid_counter = 0
                
                for i in range(len(user_data["Player"])):
                    if user_data['Player'][i] == valid_player:
                        valid_counter = i
                
                valid_order = order_type.get()
                if valid_order == 'Sell':
                    order_volume['values'] = [i+1 for i in range(user_data['Volume'][valid_counter])]
                else:
                    order_volume['values'] = [i+1 for i in range(lim_volume)] 

                order_volume.grid(row = 5,column = 1, padx = 10, pady = 10)
    
            player_button = ttk.Button(self, text='Submit to enter other details', command = volume_drop)
            player_button.grid(row = 6, column = 1, padx = 10, pady = 10)
            
            '''
            def delete():
                ipl_player.delete(0,'end')
                order_type.delete(0,'end')
                order_price.delete(0,'end')
                order_volume.delete(0,'end')
            '''

            def submit_order():
                player = ipl_player.get()
                o_type = order_type.get()
                volume = int(order_volume.get())
                price = int(order_price.get())
                
                your_order['Player'].append(player)
                your_order['Type'].append(o_type)
                your_order['Price'].append(price)
                your_order['Volume'].append(volume)
                
                if player in user_data['Player']:
                    counter = 0
                    for i in range(len(user_data['Player'])):
                        if user_data['Player'][i] == player:
                            counter = i
                    if o_type == 'Buy':
                        user_data['Volume'][counter] += volume
                    if o_type == 'Sell':
                        user_data['Volume'][counter] -= volume
                else:
                    user_data['Player'].append(player)
                    user_data['Volume'].append(volume)
    
                print(player,o_type,volume,price)
    
                ipl_player.delete(0,'end')
                order_type.delete(0,'end')
                order_price.delete(0,'end')
                order_volume.delete(0,'end')
                
                global limit
                if o_type == 'Buy':
                    game_data.at[player,'Volume'] -= volume
                    limit -= (volume*price)
                elif o_type == 'Sell':
                    game_data.at[player,'Volume'] += volume
                    limit += (price*volume)
                
                game_data.at[player,'Price'] = price
                
                print("YOUR ORDER\n",your_order)
                global df_order
                df_order = pd.DataFrame(your_order)
                #print(df_order)
                    
            submit = tk.Button(self,text = 'Submit', command = submit_order)
            submit.grid(row = 7,column = 1, padx = 10, pady = 10)
        
############ GAMEDATA PAGE #############################
class GameData(tk.Frame): 
    def __init__(self, parent, controller): 
        
######### DESIGN ##############
        tk.Frame.__init__(self, parent) 
        label = ttk.Label(self, text ="GameData", font = LARGEFONT) 
        label.grid(row = 0, column = 4, padx = 10, pady = 10) 
        button1 = ttk.Button(self, text ="Startpage", 
                            command = lambda : controller.show_frame(StartPage)) 
        button1.grid(row = 0, column = 1, padx = 10, pady = 10)
        
        player_names = ['Player '+str(i+1) for i in range(50)]
        
        def refresh3():
            columns = list(game_data.columns)
            
            num_row = len(game_data.index)
            num_col = len(game_data.columns)
            
            column_names = ['Ipl Player']+list(game_data.columns)
            for i in range(len(column_names)):
                record = tk.Entry(self)
                record.grid(row=1,column=i,padx=10,pady=10)
                added_value = column_names[i]
                record.insert(0,added_value)
            
            for i in range(50):
                record = tk.Entry(self)
                record.grid(row=i+2,column=0,padx=10,pady=10)
                added_value = player_names[i]
                record.insert(0,added_value)
            
            for i in range(num_col):
                for j in range(num_row):
                    record = tk.Entry(self)
                    record.grid(row=j+2,column=i+1,padx=10,pady=10)
                    added_value = game_data[columns[i]].iloc[j]
                    record.insert(0,added_value)
            
            my_canvas = tk.Canvas(self)
            #my_canvas.pack(side = 'left')
            yscrollbar = ttk.Scrollbar(self,orient = 'vertical', command = my_canvas.yview)
            yscrollbar.grid(row=0,column=0,padx=10,pady=10)
            my_frame = tk.Frame(my_canvas)
            my_canvas.configure(yscrollcommand=yscrollbar.set)
            my_canvas.bind('<Configure>' , lambda e: my_canvas.configure(scrollregion = my_canvas.bbox('all')))
            my_canvas.create_window((0,0),window=my_frame,anchor='nw')
        
        refresh_button = ttk.Button(self,text="Refresh Page", command = refresh3)
        refresh_button.grid(row=0,column=3)        



############# YOUR ORDERS PAGE #########################
#print(df_order)
class YourOrders(tk.Frame): 
    def __init__(self, parent, controller): 
        tk.Frame.__init__(self, parent) 
        label = ttk.Label(self, text ="YourOrders", font = LARGEFONT) 
        label.grid(row = 0, column = 4, padx = 10, pady = 10)  
        button1 = ttk.Button(self, text ="Startpage", 
                            command = lambda : controller.show_frame(StartPage)) 
        button1.grid(row = 2, column = 1, padx = 10, pady = 10)
        
        def refresh():
            df_order = pd.DataFrame(your_order)

            columns = list(df_order.columns)
            
            num_row = len(df_order.index)
            num_col = len(df_order.columns)
            
            for i in range(num_col):
                for j in range(num_row):
                    record = tk.Entry(self)
                    record.grid(row=j+2,column=i+2,padx=10,pady=10)
                    added_value = df_order[columns[i]].iloc[j]
                    record.insert(0,added_value)
        
        refresh_button = ttk.Button(self,text="REFRESH PAGE", command = refresh)
        refresh_button.grid(row=3,column=1)
            

############## USER DATA ##############
class UserData(tk.Frame): 
    def __init__(self, parent, controller): 
        tk.Frame.__init__(self, parent) 
        label = ttk.Label(self, text ="UserData", font = LARGEFONT) 
        label.grid(row = 0, column = 4, padx = 10, pady = 10) 
        button1 = ttk.Button(self, text ="Startpage", 
                            command = lambda : controller.show_frame(StartPage)) 
        button1.grid(row = 2, column = 1, padx = 10, pady = 10)
        
        def refresh2():
            
            limit_text = tk.Entry(self)
            limit_text.insert(0,limit)
            limit_text.grid(row=2,column=10)
            
            print("USER DATA: ",pd.DataFrame(user_data))
            
            df_user = pd.DataFrame(user_data)

            columns = list(df_user.columns)
            
            num_row = len(df_user.index)
            num_col = len(df_user.columns)
            
            for i in range(num_col):
                for j in range(num_row):
                    record = tk.Entry(self)
                    record.grid(row=j+2,column=i+2,padx=10,pady=10)
                    added_value = df_user[columns[i]].iloc[j]
                    record.insert(0,added_value)
        
        refresh_button = ttk.Button(self,text="REFRESH PAGE", command = refresh2)
        refresh_button.grid(row=3,column=1)
            
class DataChange(tk.Frame): 
    def __init__(self, parent, controller): 

        tk.Frame.__init__(self, parent)  
        label = ttk.Label(self, text ="DataChange", font = LARGEFONT) 
        label.grid(row = 0, column = 4, padx = 10, pady = 10) 
        button1 = ttk.Button(self, text ="Startpage", 
                            command = lambda : controller.show_frame(StartPage)) 
        button1.grid(row = 0, column = 1, padx = 10, pady = 10)
        
        label = ttk.Label(self, text ="Player", font = inputs)
        label.grid(row = 2, column = 0, padx = 10, pady = 10)
        ipl_player = ttk.Combobox(self)
        ipl_player['values'] = ['Player '+str(i+1) for i in range(len(game_data.index))]
        ipl_player.grid(row=2,column=1,padx=10,pady=10)
        
        label = ttk.Label(self, text ="FEATURE TO CHANGE", font = inputs)
        label.grid(row = 3, column = 0, padx = 10, pady = 10)
        feature = ttk.Combobox(self)
        feature['values'] = ['Consistency Index','Applauses']
        feature.grid(row=3,column=1,padx=10,pady=10)
        
        label = ttk.Label(self, text ="NEW VALUE", font = inputs)
        label.grid(row = 4, column = 0, padx = 10, pady = 10)
        feature_value = ttk.Entry(self)
        feature_value.grid(row=4,column=1,padx=10,pady=10)       

        def submit():
            player = ipl_player.get()
            option = feature.get()
            value = feature_value.get()
            
            game_data.at[player,option] = value
            
            ipl_player.delete(0,'end')
            feature.delete(0,'end')
            feature_value.delete(0,'end')

        submit_final = ttk.Button(self,text="Submit",command = submit)
        submit_final.grid(row=6,column=1,padx=10,pady=10)

app = tkinterApp() 
app.mainloop() 