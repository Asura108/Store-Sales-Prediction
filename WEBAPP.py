# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 22:18:32 2022

@author: Deep
"""
import numpy as np
import pickle
import streamlit as st

st.title("Stores Sales Predictions")

item_weight = st.number_input("Please Enter the weight of the item = ")

item_fat = st.radio("Enter the fat levels for your item",["Low Fat","Regular"],index=1)
if(item_fat=="Low Fat"):
    item_fat=0
    
else:
    item_fat=1

item_vis = st.number_input("Enter the visibility of your item = ")

item_mrp = st.number_input("Enter the MRP of your item =  ")

z = st.radio("Select the type of outlet the item is in ",["Grocery Store","Supermarket Type1","Supermarket Type2","Supermarket Type3"],index=1)

if(z=="Grocery Store"):
    Outlet_Type_Grocery_Store=1
    Outlet_Type_Supermarket_Type1=0
    Outlet_Type_Supermarket_Type2=0
    Outlet_Type_Supermarket_Type3=0
elif(z=="Supermarket Type1"):
    Outlet_Type_Grocery_Store=0
    Outlet_Type_Supermarket_Type1=1
    Outlet_Type_Supermarket_Type2=0
    Outlet_Type_Supermarket_Type3=0
elif(z=="Supermarket Type2"):
    Outlet_Type_Grocery_Store=0
    Outlet_Type_Supermarket_Type1=0
    Outlet_Type_Supermarket_Type2=1
    Outlet_Type_Supermarket_Type3=0
elif(z=="Supermarket Type3"):
    Outlet_Type_Grocery_Store=0
    Outlet_Type_Supermarket_Type1=0
    Outlet_Type_Supermarket_Type2=0
    Outlet_Type_Supermarket_Type3=1
    
k = st.radio("Select the type the item is of ",['Dairy', 'Soft Drinks', 'Meat', 'Fruits and Vegetables','Household', 'Baking Goods', 'Snack Foods', 'Frozen Foods','Breakfast', 'Health and Hygiene', 'Hard Drinks', 'Canned','Breads', 'Starchy Foods', 'Others', 'Seafood'])

if(k=="Dairy"):
    item_type_dairy=1
    item_type_SD=0
    item_type_meat=0
    item_type_fruits=0
    item_type_househ=0
    item_type_baking=0
    item_type_snack=0
    item_type_frozen=0
    item_type_breakfast=0
    item_type_health=0
    item_type_hard=0
    item_type_canned=0
    item_type_breads=0
    item_type_starchy=0
    item_type_others=0
    item_type_sea=0

elif(k=="Soft Drinks"):
    item_type_dairy=0
    item_type_SD=1
    item_type_meat=0
    item_type_fruits=0
    item_type_househ=0
    item_type_baking=0
    item_type_snack=0
    item_type_frozen=0
    item_type_breakfast=0
    item_type_health=0
    item_type_hard=0
    item_type_canned=0
    item_type_breads=0
    item_type_starchy=0
    item_type_others=0
    item_type_sea=0
    
elif(k=="Meat"):
    item_type_dairy=0
    item_type_SD=0
    item_type_meat=1
    item_type_fruits=0
    item_type_househ=0
    item_type_baking=0
    item_type_snack=0
    item_type_frozen=0
    item_type_breakfast=0
    item_type_health=0
    item_type_hard=0
    item_type_canned=0
    item_type_breads=0
    item_type_starchy=0
    item_type_others=0
    item_type_sea=0
    
elif(k=="Fruits and Vegetables"):
    item_type_dairy=0
    item_type_SD=0
    item_type_meat=0
    item_type_fruits=1
    item_type_househ=0
    item_type_baking=0
    item_type_snack=0
    item_type_frozen=0
    item_type_breakfast=0
    item_type_health=0
    item_type_hard=0
    item_type_canned=0
    item_type_breads=0
    item_type_starchy=0
    item_type_others=0
    item_type_sea=0

elif(k=="Household"):
    item_type_dairy=1
    item_type_SD=0
    item_type_meat=0
    item_type_fruits=0
    item_type_househ=0
    item_type_baking=0
    item_type_snack=0
    item_type_frozen=0
    item_type_breakfast=0
    item_type_health=0
    item_type_hard=0
    item_type_canned=0
    item_type_breads=0
    item_type_starchy=0
    item_type_others=0
    item_type_sea=0


elif(k=="Baking Goods"):
    item_type_dairy=1
    item_type_SD=0
    item_type_meat=0
    item_type_fruits=0
    item_type_househ=0
    item_type_baking=0
    item_type_snack=0
    item_type_frozen=0
    item_type_breakfast=0
    item_type_health=0
    item_type_hard=0
    item_type_canned=0
    item_type_breads=0
    item_type_starchy=0
    item_type_others=0
    item_type_sea=0


elif(k=="Snack Foods"):
    item_type_dairy=1
    item_type_SD=0
    item_type_meat=0
    item_type_fruits=0
    item_type_househ=0
    item_type_baking=0
    item_type_snack=0
    item_type_frozen=0
    item_type_breakfast=0
    item_type_health=0
    item_type_hard=0
    item_type_canned=0
    item_type_breads=0
    item_type_starchy=0
    item_type_others=0
    item_type_sea=0


elif(k=="Frozen Foods"):
    item_type_dairy=1
    item_type_SD=0
    item_type_meat=0
    item_type_fruits=0
    item_type_househ=0
    item_type_baking=0
    item_type_snack=0
    item_type_frozen=0
    item_type_breakfast=0
    item_type_health=0
    item_type_hard=0
    item_type_canned=0
    item_type_breads=0
    item_type_starchy=0
    item_type_others=0
    item_type_sea=0


elif(k=="Breakfast"):
    item_type_dairy=1
    item_type_SD=0
    item_type_meat=0
    item_type_fruits=0
    item_type_househ=0
    item_type_baking=0
    item_type_snack=0
    item_type_frozen=0
    item_type_breakfast=0
    item_type_health=0
    item_type_hard=0
    item_type_canned=0
    item_type_breads=0
    item_type_starchy=0
    item_type_others=0
    item_type_sea=0


elif(k=="Health and Hygiene"):
    item_type_dairy=1
    item_type_SD=0
    item_type_meat=0
    item_type_fruits=0
    item_type_househ=0
    item_type_baking=0
    item_type_snack=0
    item_type_frozen=0
    item_type_breakfast=0
    item_type_health=0
    item_type_hard=0
    item_type_canned=0
    item_type_breads=0
    item_type_starchy=0
    item_type_others=0
    item_type_sea=0
    
elif(k=="Hard Drinks"):
    item_type_dairy=1
    item_type_SD=0
    item_type_meat=0
    item_type_fruits=0
    item_type_househ=0
    item_type_baking=0
    item_type_snack=0
    item_type_frozen=0
    item_type_breakfast=0
    item_type_health=0
    item_type_hard=0
    item_type_canned=0
    item_type_breads=0
    item_type_starchy=0
    item_type_others=0
    item_type_sea=0
    
elif(k=="Canned"):
    item_type_dairy=1
    item_type_SD=0
    item_type_meat=0
    item_type_fruits=0
    item_type_househ=0
    item_type_baking=0
    item_type_snack=0
    item_type_frozen=0
    item_type_breakfast=0
    item_type_health=0
    item_type_hard=0
    item_type_canned=0
    item_type_breads=0
    item_type_starchy=0
    item_type_others=0
    item_type_sea=0
    
elif(k=="Breads"):
    item_type_dairy=1
    item_type_SD=0
    item_type_meat=0
    item_type_fruits=0
    item_type_househ=0
    item_type_baking=0
    item_type_snack=0
    item_type_frozen=0
    item_type_breakfast=0
    item_type_health=0
    item_type_hard=0
    item_type_canned=0
    item_type_breads=0
    item_type_starchy=0
    item_type_others=0
    item_type_sea=0
    
elif(k=="Starchy Foods"):
    item_type_dairy=1
    item_type_SD=0
    item_type_meat=0
    item_type_fruits=0
    item_type_househ=0
    item_type_baking=0
    item_type_snack=0
    item_type_frozen=0
    item_type_breakfast=0
    item_type_health=0
    item_type_hard=0
    item_type_canned=0
    item_type_breads=0
    item_type_starchy=0
    item_type_others=0
    item_type_sea=0
    
elif(k=="Others"):
    item_type_dairy=1
    item_type_SD=0
    item_type_meat=0
    item_type_fruits=0
    item_type_househ=0
    item_type_baking=0
    item_type_snack=0
    item_type_frozen=0
    item_type_breakfast=0
    item_type_health=0
    item_type_hard=0
    item_type_canned=0
    item_type_breads=0
    item_type_starchy=0
    item_type_others=0
    item_type_sea=0
    
elif(k=="Seafood"):
    item_type_dairy=1
    item_type_SD=0
    item_type_meat=0
    item_type_fruits=0
    item_type_househ=0
    item_type_baking=0
    item_type_snack=0
    item_type_frozen=0
    item_type_breakfast=0
    item_type_health=0
    item_type_hard=0
    item_type_canned=0
    item_type_breads=0
    item_type_starchy=0
    item_type_others=0
    item_type_sea=0


pp = st.radio("Select the outlet location type where the item is to be sold",['Tier 1','Tier 2','Tier 3'])

if(pp=="Tier 1"):
    outlet_type_t1=1
    outlet_type_t2=0
    outlet_type_t3=0
    
elif(pp=="Tier 2"):
    outlet_type_t1=0
    outlet_type_t2=1
    outlet_type_t3=0
    
elif(pp=="Tier 3"):
    outlet_type_t1=0
    outlet_type_t2=0
    outlet_type_t3=1
  
Lin_reg = pickle.load(open('Lin_reg', 'rb'))
Dec_trees = pickle.load(open('Dec_trees', 'rb'))
Ran_for = pickle.load(open('Ran_for', 'rb'))    
    
h = [item_weight,item_fat,item_vis,item_mrp,Outlet_Type_Grocery_Store,Outlet_Type_Supermarket_Type1,Outlet_Type_Supermarket_Type2,Outlet_Type_Supermarket_Type3,item_type_baking,item_type_breads,item_type_breakfast,item_type_canned,item_type_dairy,item_type_frozen,item_type_fruits,item_type_hard,item_type_health,item_type_househ,item_type_meat,item_type_others,item_type_sea,item_type_snack,item_type_SD,item_type_starchy,outlet_type_t1,outlet_type_t2,outlet_type_t3]

h=np.array(h)

h=h.reshape(1,27)

Pred_Lin = Lin_reg.predict(h)
Pred_Dec = Dec_trees.predict(h)    
Pred_Ran = Ran_for.predict(h)    
    
Final_Pred = (Pred_Lin*0.4 + Pred_Dec*0.2 + Pred_Ran*0.4)

if st.button("CLICK HERE TO PREDICT SALES PRICE FOR THE ITEM"):
    st.write(Final_Pred)




