from flask import Flask, render_template, request

import pickle as pickle

import numpy as np

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    Final_Pred=0
    if request.method == 'POST':

        Lin_reg = pickle.load(open('Lin_reg', 'rb'))
        Dec_trees = pickle.load(open('Dec_trees', 'rb'))
        Ran_for = pickle.load(open('Ran_for', 'rb'))

        item_weight = request.form.get('item_weight')

        item_fat = request.form.get('item_fat')

        item_vis = request.form.get('item_vis')
        item_mrp = request.form.get('item_mrp')

        Outlet_Type_Grocery_Store = 0
        Outlet_Type_Supermarket_Type1=0
        Outlet_Type_Supermarket_Type2=0
        Outlet_Type_Supermarket_Type3=0
        item_type_baking=0
        item_type_breads=0
        item_type_breakfast=0
        item_type_canned=0
        item_type_dairy=0
        item_type_frozen=0
        item_type_fruits=0
        item_type_hard=0
        item_type_health=0
        item_type_househ=0
        item_type_meat=0
        item_type_others=0
        item_type_sea=0
        item_type_snack=0
        item_type_SD=0
        item_type_starchy=0
        outlet_type_t1=0
        outlet_type_t2=0
        outlet_type_t3=0
        Final_Pred = 0




        z = request.form.get('outlet_type')
        if  (z == 0):
            Outlet_Type_Grocery_Store = 1
            Outlet_Type_Supermarket_Type1 = 0
            Outlet_Type_Supermarket_Type2 = 0
            Outlet_Type_Supermarket_Type3 = 0
        elif (z == 1):
            Outlet_Type_Grocery_Store = 0
            Outlet_Type_Supermarket_Type1 = 1
            Outlet_Type_Supermarket_Type2 = 0
            Outlet_Type_Supermarket_Type3 = 0
        elif (z == 2):
            Outlet_Type_Grocery_Store = 0
            Outlet_Type_Supermarket_Type1 = 0
            Outlet_Type_Supermarket_Type2 = 1
            Outlet_Type_Supermarket_Type3 = 0
        elif (z == 3):
            Outlet_Type_Grocery_Store = 0
            Outlet_Type_Supermarket_Type1 = 0
            Outlet_Type_Supermarket_Type2 = 0
            Outlet_Type_Supermarket_Type3 = 1





        k = request.form.get('item_type')
        if (k == 0):
            item_type_dairy = 1
            item_type_SD = 0
            item_type_meat = 0
            item_type_fruits = 0
            item_type_househ = 0
            item_type_baking = 0
            item_type_snack = 0
            item_type_frozen = 0
            item_type_breakfast = 0
            item_type_health = 0
            item_type_hard = 0
            item_type_canned = 0
            item_type_breads = 0
            item_type_starchy = 0
            item_type_others = 0
            item_type_sea = 0

        elif (k == 1):
            item_type_dairy = 0
            item_type_SD = 1
            item_type_meat = 0
            item_type_fruits = 0
            item_type_househ = 0
            item_type_baking = 0
            item_type_snack = 0
            item_type_frozen = 0
            item_type_breakfast = 0
            item_type_health = 0
            item_type_hard = 0
            item_type_canned = 0
            item_type_breads = 0
            item_type_starchy = 0
            item_type_others = 0
            item_type_sea = 0

        elif (k == 2):
            item_type_dairy = 0
            item_type_SD = 0
            item_type_meat = 1
            item_type_fruits = 0
            item_type_househ = 0
            item_type_baking = 0
            item_type_snack = 0
            item_type_frozen = 0
            item_type_breakfast = 0
            item_type_health = 0
            item_type_hard = 0
            item_type_canned = 0
            item_type_breads = 0
            item_type_starchy = 0
            item_type_others = 0
            item_type_sea = 0

        elif (k == 3):
            item_type_dairy = 0
            item_type_SD = 0
            item_type_meat = 0
            item_type_fruits = 1
            item_type_househ = 0
            item_type_baking = 0
            item_type_snack = 0
            item_type_frozen = 0
            item_type_breakfast = 0
            item_type_health = 0
            item_type_hard = 0
            item_type_canned = 0
            item_type_breads = 0
            item_type_starchy = 0
            item_type_others = 0
            item_type_sea = 0

        elif (k == 4):
            item_type_dairy = 0
            item_type_SD = 0
            item_type_meat = 0
            item_type_fruits = 0
            item_type_househ = 1
            item_type_baking = 0
            item_type_snack = 0
            item_type_frozen = 0
            item_type_breakfast = 0
            item_type_health = 0
            item_type_hard = 0
            item_type_canned = 0
            item_type_breads = 0
            item_type_starchy = 0
            item_type_others = 0
            item_type_sea = 0


        elif (k == 5):
            item_type_dairy = 0
            item_type_SD = 0
            item_type_meat = 0
            item_type_fruits = 0
            item_type_househ = 0
            item_type_baking = 1
            item_type_snack = 0
            item_type_frozen = 0
            item_type_breakfast = 0
            item_type_health = 0
            item_type_hard = 0
            item_type_canned = 0
            item_type_breads = 0
            item_type_starchy = 0
            item_type_others = 0
            item_type_sea = 0


        elif (k == 6):
            item_type_dairy = 0
            item_type_SD = 0
            item_type_meat = 0
            item_type_fruits = 0
            item_type_househ = 0
            item_type_baking = 0
            item_type_snack = 1
            item_type_frozen = 0
            item_type_breakfast = 0
            item_type_health = 0
            item_type_hard = 0
            item_type_canned = 0
            item_type_breads = 0
            item_type_starchy = 0
            item_type_others = 0
            item_type_sea = 0


        elif (k == 7):
            item_type_dairy = 0
            item_type_SD = 0
            item_type_meat = 0
            item_type_fruits = 0
            item_type_househ = 0
            item_type_baking = 0
            item_type_snack = 0
            item_type_frozen = 1
            item_type_breakfast = 0
            item_type_health = 0
            item_type_hard = 0
            item_type_canned = 0
            item_type_breads = 0
            item_type_starchy = 0
            item_type_others = 0
            item_type_sea = 0


        elif (k == 8):
            item_type_dairy = 0
            item_type_SD = 0
            item_type_meat = 0
            item_type_fruits = 0
            item_type_househ = 0
            item_type_baking = 0
            item_type_snack = 0
            item_type_frozen = 0
            item_type_breakfast = 1
            item_type_health = 0
            item_type_hard = 0
            item_type_canned = 0
            item_type_breads = 0
            item_type_starchy = 0
            item_type_others = 0
            item_type_sea = 0


        elif (k == 9):
            item_type_dairy = 0
            item_type_SD = 0
            item_type_meat = 0
            item_type_fruits = 0
            item_type_househ = 0
            item_type_baking = 0
            item_type_snack = 0
            item_type_frozen = 0
            item_type_breakfast = 0
            item_type_health = 1
            item_type_hard = 0
            item_type_canned = 0
            item_type_breads = 0
            item_type_starchy = 0
            item_type_others = 0
            item_type_sea = 0

        elif (k == 10):
            item_type_dairy = 0
            item_type_SD = 0
            item_type_meat = 0
            item_type_fruits = 0
            item_type_househ = 0
            item_type_baking = 0
            item_type_snack = 0
            item_type_frozen = 0
            item_type_breakfast = 0
            item_type_health = 0
            item_type_hard = 1
            item_type_canned = 0
            item_type_breads = 0
            item_type_starchy = 0
            item_type_others = 0
            item_type_sea = 0

        elif (k ==11):
            item_type_dairy = 0
            item_type_SD = 0
            item_type_meat = 0
            item_type_fruits = 0
            item_type_househ = 0
            item_type_baking = 0
            item_type_snack = 0
            item_type_frozen = 0
            item_type_breakfast = 0
            item_type_health = 0
            item_type_hard = 0
            item_type_canned = 1
            item_type_breads = 0
            item_type_starchy = 0
            item_type_others = 0
            item_type_sea = 0

        elif (k ==12):
            item_type_dairy = 0
            item_type_SD = 0
            item_type_meat = 0
            item_type_fruits = 0
            item_type_househ = 0
            item_type_baking = 0
            item_type_snack = 0
            item_type_frozen = 0
            item_type_breakfast = 0
            item_type_health = 0
            item_type_hard = 0
            item_type_canned = 0
            item_type_breads = 1
            item_type_starchy = 0
            item_type_others = 0
            item_type_sea = 0

        elif (k ==13):
            item_type_dairy = 0
            item_type_SD = 0
            item_type_meat = 0
            item_type_fruits = 0
            item_type_househ = 0
            item_type_baking = 0
            item_type_snack = 0
            item_type_frozen = 0
            item_type_breakfast = 0
            item_type_health = 0
            item_type_hard = 0
            item_type_canned = 0
            item_type_breads = 0
            item_type_starchy = 1
            item_type_others = 0
            item_type_sea = 0

        elif (k == 14):
            item_type_dairy = 0
            item_type_SD = 0
            item_type_meat = 0
            item_type_fruits = 0
            item_type_househ = 0
            item_type_baking = 0
            item_type_snack = 0
            item_type_frozen = 0
            item_type_breakfast = 0
            item_type_health = 0
            item_type_hard = 0
            item_type_canned = 0
            item_type_breads = 0
            item_type_starchy = 0
            item_type_others = 1
            item_type_sea = 0

        elif k == 15:
            item_type_dairy = 0
            item_type_SD = 0
            item_type_meat = 0
            item_type_fruits = 0
            item_type_househ = 0
            item_type_baking = 0
            item_type_snack = 0
            item_type_frozen = 0
            item_type_breakfast = 0
            item_type_health = 0
            item_type_hard = 0
            item_type_canned = 0
            item_type_breads = 0
            item_type_starchy = 0
            item_type_others = 0
            item_type_sea = 1


        pp = request.form.get('outlet_tier')
        if pp ==0:
            outlet_type_t1 = 1
            outlet_type_t2 = 0
            outlet_type_t3 = 0

        elif pp ==1:
            outlet_type_t1 = 0
            outlet_type_t2 = 1
            outlet_type_t3 = 0

        elif pp == 2:
            outlet_type_t1 = 0
            outlet_type_t2 = 0
            outlet_type_t3 = 1


        h = [item_weight,item_fat,item_vis,item_mrp,Outlet_Type_Grocery_Store,Outlet_Type_Supermarket_Type1,Outlet_Type_Supermarket_Type2,Outlet_Type_Supermarket_Type3,item_type_baking,item_type_breads,item_type_breakfast,item_type_canned,item_type_dairy,item_type_frozen,item_type_fruits,item_type_hard,item_type_health,item_type_househ,item_type_meat,item_type_others,item_type_sea,item_type_snack,item_type_SD,item_type_starchy,outlet_type_t1,outlet_type_t2,outlet_type_t3]

        h=np.array(h)

        h = h.reshape(1,27)

        Pred_Lin = Lin_reg.predict(h)
        Pred_Dec = Dec_trees.predict(h)
        Pred_Ran = Ran_for.predict(h)
        Final_Pred = (Pred_Lin*0.4 + Pred_Dec*0.2 + Pred_Ran*0.4)
        print(Final_Pred)

    return render_template('Form.html', prediction=Final_Pred)


if __name__ == '__main__' :
    app.run(debug=True)