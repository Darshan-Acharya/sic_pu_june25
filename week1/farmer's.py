def farmer_sale_calculator():
    def farmer_sale_calculator():
    total_acres = 80
    segments = 5
    acre_per_segment = total_acres / segments
    crops = ['Tomoto', 'Potato', 'Cabbagge', 'sunflower', 'sugarcane']
    tomoto_yeild = 0.3*(acre_per_segment)*(10) + 0.7*(acre_per_segment)*(12)
    pototo_yeild = 10*acre_per_segment
    cabbage_yeild = 14*acre_per_segment
    sunflower_yeild = 0.7*acre_per_segment
    sugarcane_yeild = 45*acre_per_segment
    yeilds = [tomoto_yeild,  pototo_yeild, cabbage_yeild, sunflower_yeild, sugarcane_yeild]
    price_list = [7000, 20000, 24000, 200000, 4000]#per tonn converstion
    total_sellings = 0
    print("The overall sales acheived by the Farmer mahesh from his 80 acres of land is as fallows")
    for i in range(len(yeilds)):
        print("yeild of the %4s is %0.2f tonns and It's overall selling price is %0.2f Rupees"%(crops[i], yeilds[i], (price_list[i]*yeilds[i])))
        total_sellings += (price_list[i]*yeilds[i])
    print(f"Total selling price of entire land of mahesh is {total_sellings} rupees ")
farmer_sale_calculator()
