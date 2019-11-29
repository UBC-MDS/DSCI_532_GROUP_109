import pandas as pd
import altair as alt
def make_titanic_plot(deck_level='A'):
    titanic_df = pd.read_csv("../data/titanic.csv").fillna("None")
    
    cabin_locations = {"A36": (350, 1.0), "A37": (350, 6.0), "A32": (400, 6.0), "A30": (400, 5.0), "A31": (400, 2.0), "A33": (400, 1.0), "A28": (405, 6.0), "A26": (405, 5.0), "A27": (405, 2.0),
                       "A29": (405, 1.0), "A34": (395, 6.0), "A35": (395, 1.0), "A24": (410, 6.0), "A22": (410, 5.0), "A23": (410, 2.0), "A25": (410, 1.0), "A20": (415, 6.0), "A18": (415, 5.0),
                       "A19": (415, 2.0), "A21": (415, 1.0), "A16": (420, 6.0), "A14": (420, 5.0), "A15": (420, 2.0), "A17": (420, 1.0), "A12": (425, 6.0), "A10": (425, 5.0), "A9":  (425, 2.0),
                       "A11": (425, 1.0), "A8": ( 430, 6.0),  "A6": (430, 5.0), "A5":  (430, 2.0), "A7":  (430, 1.0), "A4":  (435, 6.0), "A2":  (435, 4.0), "A1":  (435, 3.0), "A3":  (435, 1.0),
                       
                       "B90": (345, 6.0), "B94": (340, 6.0), "B96": (335, 6.0), "B98": (330, 6.0), "B92": (345, 5.0), "B91": (345, 1.0), "B101": (395, 3.0), "B102": (395, 4.0), "B100": (385, 4.0),
                       "B99": (385, 3.0), "B58": (400, 6.0), "B88": (350, 6.0), "B84": (355, 6.0), "B86": (355, 5.0), "B85": (355, 1.0), "B82": (360, 6.0), "B78": (365, 6.0), "B76": (370, 6.0),
                       "B72": (375, 6.0), "B70": (380, 6.0), "B66": (385, 6.0), "B64": (390, 6.0), "B60": (395, 6.0), "B80": (365, 5.0), "B74": (375, 5.0), "B68": (385, 5.0), "B62":  (395, 5.0),
                       "B79": (365, 1.0), "B73": (375, 1.0), "B67": (385, 1.0), "B52": (405, 5.0), "B51": (405, 1.0), "B61":  (395, 1.0), "B48": (425, 6.0), "B46": (425, 5.0), "B47": (425, 2.0),
                       "B49": (425, 1.0), "B44": (430, 6.0), "B42": (430, 5.0), "B43": (430, 2.0), "B45": (430, 1.0), "B40":  (435, 6.0), "B38": (435, 5.0), "B37": (435, 2.0), "B39": (435, 1.0),
                       "B34": (440, 6.0), "B32": (440, 5.0), "B30": (440, 4.0), "B31": (440, 3.0), "B33": (440, 2.0), "B35":  (440, 1.0), "B28": (445, 6.0), "B26": (445, 5.0), "B24": (445, 4.0),
                       "B25": (445, 3.0), "B27": (445, 2.0), "B29": (445, 1.0), "B22": (450, 6.0), "B20": (450, 5.0), "B18":  (450, 4.0), "B19": (450, 3.0), "B21": (450, 2.0), "B23": (450, 1.0),
                       "B16": (455, 6.0), "B14": (455, 5.0), "B12": (455, 4.0), "B11": (455, 3.0), "B15": (455, 2.0), "B17":  (455, 1.0), "B10": (460, 5.0), "B8": (460, 4.0), "B7": (460, 3.0),
                       "B9": (460, 2.0),  "B6": (465, 6.0), "B4":  (465, 5.0), "B3": (465, 4.0), "B1": (465, 3.0), "B3": (465, 2.0), "B5": (465, 1.0)}
                       

    cabin_locations_df = pd.DataFrame(cabin_locations).T.reset_index()
    cabin_locations_df["deck"] = cabin_locations_df["index"].apply(lambda x: x[0])
    cabin_locations_df = cabin_locations_df.set_index(["deck", "index"])
    cabin_locations_df.index.names = ["deck", "cabin"]
    cabin_locations_df.columns = ["cabin_x", "cabin_y"]
    
    titanic_df_with_cabin_coords = pd.merge(titanic_df, cabin_locations_df, left_on = "cabin", right_on = "cabin")
    titanic_df_with_cabin_coords["deck"] = titanic_df_with_cabin_coords["cabin"].apply(lambda x: x[0])
    titanic_passengers_by_cabin = titanic_df_with_cabin_coords.set_index(["cabin","name"]).sort_index()
    
    for cabins in titanic_passengers_by_cabin.index.levels[0]:
        if titanic_passengers_by_cabin.loc[cabins].shape[0] > 1:
            i=0
            passengers = list(titanic_passengers_by_cabin.loc[cabins].index)
            for passenger in passengers:
                if i==0:
                    shift_x = 1
                    shift_y = 0.25
                if i==1:
                    shift_x = -1
                    shift_y = 0.25
                if i==2:
                    shift_x = -1
                    shift_y = -0.25
                if i==3:
                    shift_x = 1
                    shift_y = -0.25

                titanic_passengers_by_cabin.loc[cabins].at[passenger, "cabin_x"] = float(titanic_passengers_by_cabin.loc[cabins].at[passenger, "cabin_x"]) + shift_x
                titanic_passengers_by_cabin.loc[cabins].at[passenger, "cabin_y"] = float(titanic_passengers_by_cabin.loc[cabins].at[passenger, "cabin_y"]) + shift_y
                i+=1
    
    ship_outline_1 = pd.DataFrame({"x" : [305, 325, 470, 475, 477], "y" : [3.5, 7, 7, 6, 5]})
    ship_outline_2 = pd.DataFrame({"x" : [305, 325, 470, 475, 477], "y" :  [3.5, 0, 0, 1, 2]})
    ship_outline_3 = pd.DataFrame({"x" : [477,477], "y" :  [2, 5]})

    chart_ship_outline_1 = alt.Chart(ship_outline_1).mark_line().encode(
        alt.X('x:Q'),
        alt.Y('y:Q')
    )
    chart_ship_outline_2 = alt.Chart(ship_outline_2).mark_line().encode(
        alt.X('x:Q'),
        alt.Y('y:Q')
    )
    chart_ship_outline_3 = alt.Chart(ship_outline_3).mark_line().encode(
        alt.X('x:Q'),
        alt.Y('y:Q')
    )
    chart_ship_outline = chart_ship_outline_1 + chart_ship_outline_2 + chart_ship_outline_3
    
    cabin_plot = alt.Chart(cabin_locations_df.loc[deck_level]).mark_square(size = 1400, fill = "None", stroke = "black", opacity = 0.3).encode(
        alt.X('cabin_x:Q', title = "", scale=alt.Scale(domain = [300,480])),
        alt.Y('cabin_y:Q', title = "", scale=alt.Scale(domain = [-1,7.5]))
    ).properties(width = 1500, height = 400)
    titanic_passengers_by_cabin = titanic_passengers_by_cabin.reset_index().set_index(["deck","cabin"])
    titanic_passengers_by_cabin["survived"] = titanic_passengers_by_cabin["survived"].map({0:"Passenger Died", 1:"Passenger Survived"})
    
    passenger_plot = alt.Chart(titanic_passengers_by_cabin.loc[deck_level]).mark_point(size = 250, stroke = "black", filled = True, opacity = 1).encode(
        alt.X('cabin_x:Q', scale=alt.Scale(domain = [300,480])),
        alt.Y('cabin_y:Q', scale=alt.Scale(domain = [-1,7.5])),
        alt.Color('survived:N', scale=alt.Scale(range = ['red','white']), 
                                legend = alt.Legend(titleFontSize = 0, labelFontSize = 17)),
        tooltip=['name:N', 'sex:N', 'age:O']
    ).properties(width = 1500, height = 400, title = "Fate of titanic passengers by cabin location on deck {}".format(deck_level))
    
    full_plot = (cabin_plot + passenger_plot + chart_ship_outline
                ).configure_title(fontSize = 20
                ).configure_legend(orient='bottom')
    
    return full_plot

def make_class_plot():
    titanic_df = pd.read_csv("../data/titanic.csv").fillna("None")
    class_survived_df = titanic_df[['pclass','survived']]
    source_1 = class_survived_df.groupby('pclass').mean()*100
    source_2 = source_1.reset_index()
    chart = alt.Chart(source_2).mark_bar(size = 10, color = "red").encode(
            alt.X('survived:Q', title = "Rate of Survival"),
            alt.Y("pclass:O", title = "Class")
        ).properties(title = "Survival Rate by Class", width = 500, height=50)
    return chart

def make_deck_plot():
    titanic_deck_df = pd.read_csv("../data/wrangled_titanic_df.csv").fillna("None")
    titanic_deck_df['survived'] = titanic_deck_df['survived'].map({'Passenger Survived':1, 'Passenger Died':0})
    titanic_deck_df = titanic_deck_df.groupby('deck').mean()*100
    titanic_deck_df = titanic_deck_df.reset_index()
    chart = alt.Chart(titanic_deck_df).mark_bar(size = 10, color = "red").encode(
            alt.X('survived:Q', title = "Rate of Survival"),
            alt.Y("deck:O", title = "Deck")
        ).properties(title = "Survival Rate by Deck", width = 500, height=50)
    return chart