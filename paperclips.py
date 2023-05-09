import tkinter as tk

class PaperclipApp:
    def __init__(self, master):
        self.master = master
        self.paperclips = 0
        self.wire = 0
        self.auto_builders = 0
        self.auto_builder_cost = 10
        self.money = 500
        self.paperclip_sell_price = 1.01
        self.paperclip_sell_upgrade_cost = 50
        self.wire_cost = 1;
        self.wire_auto_buy_bought = False
        self.wire_auto_buy_enabled = False

        self.master.title('Universal Paperclips')

        self.money_label = tk.Label(self.master, text='Money: $100', font=('Arial', 16))
        self.money_label.pack(pady=10)

        self.paperclip_label = tk.Label(self.master, text='Paperclips: 0', font=('Arial', 16))
        self.paperclip_label.pack(pady=10)

        self.wire_label = tk.Label(self.master, text='Wire: 0', font=('Arial', 16))
        self.wire_label.pack(pady=10)

        self.make_paperclip_button = tk.Button(self.master, text='Make Paperclip', font=('Arial', 14), command=self.make_paperclip)
        self.make_paperclip_button.pack(pady=10)

        self.buy_wire_label = tk.Label(self.master, text=f'Buy Wire (Cost: ${self.wire_cost}/unit)', font=('Arial', 14))
        self.buy_wire_label.pack()

        self.auto_buy_wire_button = tk.Button(self.master, text=f"Buy Wire Auto $200", font=('Arial', 14), command=self.buy_wire_auto_check)
        self.auto_buy_wire_button.pack()

        self.wire_input = tk.Entry(self.master)
        self.wire_input.pack(pady=10)

        self.buy_wire_button = tk.Button(self.master, text='Buy Wire', font=('Arial', 14), command=self.buy_wire)
        self.buy_wire_button.pack(pady=10)

        self.auto_builder_label = tk.Label(self.master, text='Auto Builders: 0', font=('Arial', 16))
        self.auto_builder_label.pack(pady=10)

        self.buy_auto_builder_button = tk.Button(self.master, text=f'Buy Auto Builder (Cost: {self.auto_builder_cost} paperclips)', font=('Arial', 14), command=self.buy_auto_builder)
        self.buy_auto_builder_button.pack(pady=10)

        self.sell_paperclip_button = tk.Button(self.master, text=f'Sell Paperclips ($0.1/pc)', font=('Arial', 14), command=self.sell_paperclips)
        self.sell_paperclip_button.pack(pady=10)

        self.upgrade_paperclip_sell_button = tk.Button(self.master, text=f'Upgrade Paperclip Sell Price (Cost: ${self.paperclip_sell_upgrade_cost})', font=('Arial', 14), command=self.upgrade_paperclip_sell)
        self.upgrade_paperclip_sell_button.pack(pady=10)

    
        self.master.after(1000, self.update_auto_builders)

    def make_paperclip(self):
        if self.wire_auto_buy_enabled and self.wire == 0 and self.money >= self.wire_cost:
            self.money -= self.wire_cost
            self.wire += 1
            self.update_labels()
        elif self.wire >= 1:
            self.paperclips += 1
            self.wire -= 1
            self.update_labels()
        else:
            return

    def buy_wire(self):
        try:
            wire_units = int(self.wire_input.get())
        except:
            wire_units = 1
        cost = wire_units * self.wire_cost

        if self.money >= cost:
            self.money -= cost
            self.wire += wire_units
            self.update_labels()

    def buy_wire_auto_check(self):
        if not self.wire_auto_buy_bought:
            self.buy_auto_wire_buy()
            return

        if self.wire_auto_buy_enabled:
            self.wire_auto_buy_enabled = False
        else:
            self.wire_auto_buy_enabled = True
        self.update_labels()
            
    def buy_auto_wire_buy(self):
        cost = 200
        if self.money < cost:
            return
        self.money -= cost
        self.wire_auto_buy_bought = True;
        self.update_labels()

    def buy_auto_builder(self):
        if self.paperclips >= self.auto_builder_cost:
            self.paperclips -= self.auto_builder_cost
            self.auto_builders += 1
            self.auto_builder_cost *= 2
            self.buy_auto_builder_button.config(text=f'Buy Auto Builder (Cost: {self.auto_builder_cost} paperclips)')
            self.update_labels()

    def sell_paperclips(self):
        revenue = self.paperclips * self.paperclip_sell_price
        self.money += revenue
        self.paperclips = 0
        self.update_labels()

    def upgrade_paperclip_sell(self):
        if self.money >= self.paperclip_sell_upgrade_cost:
            self.money -= self.paperclip_sell_upgrade_cost
            self.paperclip_sell_price *= 2
            self.paperclip_sell_upgrade_cost *= 2
            self.upgrade_paperclip_sell_button.config(text=f'Upgrade Paperclip Sell Price (Cost: ${self.paperclip_sell_upgrade_cost})')
            self.update_labels()

    def update_auto_builders(self):
        for _ in range(self.auto_builders):
            self.make_paperclip()
        self.master.after(1000, self.update_auto_builders)




    def update_labels(self):
        self.money_label.config(text=f'Money: ${self.money:.2f}')
        self.paperclip_label.config(text=f'Paperclips: {self.paperclips}')
        self.wire_label.config(text=f'Wire: {self.wire}')
        self.auto_builder_label.config(text=f'Auto Builders: {self.auto_builders}')
        self.sell_paperclip_button.config(text=f'Sell Paperclips (${self.paperclip_sell_price:.2f}/pc)')
        if self.wire_auto_buy_bought:
            if self.wire_auto_buy_enabled:
                self.auto_buy_wire_button.config(text=f'Auto-buying wire')
            else:
                self.auto_buy_wire_button.config(text=f'not Auto-buying wire')

def main():
    root = tk.Tk()
    app = PaperclipApp(root)
    root.mainloop()

if __name__ == '__main__':
    main()


