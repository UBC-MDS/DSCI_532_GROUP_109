import pandas as pd
import altair as alt

def make_titanic_plot(deck_level='B'):
    """
    Function which plots the fate of each passenger on the titanic and shows their cabin location.

    Arguments:
    deck_level (string) desired deck to be shown in plot, defaults to deck 'B'. Options are 'A'-'G'.
    """
    #load titanic data set
    titanic_df = pd.read_csv("data/titanic.csv").fillna("None")
    
    #get cabin coordinates for plotting
    cabin_locations_df = pd.read_csv("data/cabin_locations_df.csv").set_index(["deck", "cabin"])
    
    #get wrangled titanic data
    titanic_passengers_by_cabin = pd.read_csv("data/wrangled_titanic_df.csv")

    #draw ship outline for plot
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
    
    #plotting cabins
    cabin_plot = alt.Chart(cabin_locations_df.loc[deck_level]).mark_square(size = 600, fill = "black", stroke = "black", opacity = 0.3).encode(
        alt.X('cabin_x:Q', title = "", scale=alt.Scale(domain = [300,480])),
        alt.Y('cabin_y:Q', title = "", scale=alt.Scale(domain = [-1,7.5]))
    ).properties(width = 1100, height = 300)
    
    titanic_passengers_by_cabin = titanic_passengers_by_cabin.reset_index().set_index(["deck","cabin"])
    titanic_passengers_by_cabin["survived"] = titanic_passengers_by_cabin["survived"].map({0:"Passenger Died", 1:"Passenger Survived"})
    
    #plotting passenger points
    passenger_plot = alt.Chart(titanic_passengers_by_cabin.loc[deck_level].reset_index()).mark_point(size = 80, stroke = "black", filled = True, opacity = 1).encode(
        alt.X('cabin_x:Q', scale=alt.Scale(domain = [300,480])),
        alt.Y('cabin_y:Q', scale=alt.Scale(domain = [-1,7.5])),
        alt.Color('survived:N', scale=alt.Scale(range = ['red','white']), 
                                legend = alt.Legend(titleFontSize = 0, labelFontSize = 17)),
        tooltip=['name:N', 'sex:N', 'age:O', 'cabin:N']
    ).properties(width = 1100, height = 300, title = "Fate of Titanic Passengers by Cabin Location on Deck {}".format(deck_level))
    
    #combine passenger, cabin and ship outline
    full_plot = (cabin_plot + passenger_plot + chart_ship_outline
            ).configure_title(fontSize = 20
            ).configure_legend(orient='bottom'
            ).configure_axis(grid=False, labelColor = "white", tickColor = "white", domainColor = "white"
            ).configure_view(stroke = "transparent")  
    
    return full_plot




def make_class_plot():
    """
    Function which plots the survival rate of titanic passengers as a function of passenger class
    """
    titanic_df = pd.read_csv("data/titanic.csv").fillna("None")
    class_survived_df = titanic_df[['pclass','survived']]
    source_1 = class_survived_df.groupby('pclass').mean()*100
    source_2 = source_1.reset_index()

    chart = alt.Chart(source_2).mark_bar(size = 30, fill = "#1f77b4", stroke = "1f77b4").encode(
            alt.X('survived:Q', title = "Rate of Survival (%)"),
            alt.Y("pclass:O", title = "Class")
        ).properties(title = "Survival Rate by Class", width = 600, height=250
        ).configure_axis(grid=False, titleFontSize=16, labelFontSize = 16
        ).configure_title(fontSize = 20)
    return chart




def make_deck_plot():
    """
    Function which plots the survival rate of titanic passengers as a function of deck level of their cabin
    """
    titanic_deck_df = pd.read_csv("data/wrangled_titanic_df.csv").fillna("None")
    titanic_deck_df = titanic_deck_df.reset_index().set_index(["deck","cabin"])
    titanic_deck_df = titanic_deck_df.groupby('deck').mean()*100
    titanic_deck_df = titanic_deck_df.reset_index()

    chart = alt.Chart(titanic_deck_df).mark_bar(size = 20, fill = "#1f77b4", stroke = "1f77b4").encode(
            alt.X('survived:Q', title = "Rate of Survival (%)", scale = alt.Scale(domain = [0, 80])),
            alt.Y("deck:O", title = "Deck")
        ).properties(title = "Survival Rate by Deck", width = 600, height=250
        ).configure_axis(grid=False, titleFontSize=18, labelFontSize = 16
        ).configure_title(fontSize = 20)
    return chart




def make_deck_legend(deck_level='B'):
    """
    Function which plots the deck levels on the titanic, and highlights a desired deck.

    Arguments:
    deck_level (string) desired deck to be highlighted, defaults to deck 'B'. Options are 'A'-'G'.
    """
    #plot deck outline
    deck_legend_frame = pd.DataFrame({"x" : [0, 0, 10, 10],
                                      "y" : [0, 700, 700, 0]})

    deck_legend_outline = alt.Chart(deck_legend_frame).mark_line().encode(
        alt.X('x:Q'),
        alt.Y('y:Q')).properties(
        title = "Deck Levels")
   
    legend_labels = pd.DataFrame({"x" : [5, 5, 5, 5, 5, 5, 5],
                                "y" : [50, 150, 250, 350, 450, 550, 650],
                                "label" : ["G", "F", "E", "D", "C", "B", "A"]})

    points = alt.Chart(legend_labels).mark_point(size=0).encode(
        alt.X('x:Q', scale=alt.Scale(domain = [0,10])),
        alt.Y('y:Q', scale=alt.Scale(domain = [0,700]))
    )

    #label levels
    text = points.mark_text(
        align='center',
        baseline='middle',
        size = 16
    ).encode(
        text='label'
    )  

    #highlight desired level
    current_level = alt.Chart(legend_labels.set_index("label").loc[[deck_level]]).mark_square(size = 1400, color = "black", opacity = 0.3).encode(
        alt.X('x:Q'),
        alt.Y('y:Q')
    )

    deck_levels = []

    for i in range(0, 7):
        level = pd.DataFrame({"x" : [0, 10],
                              "y" : [(100*i), (100*i)]})
        deck_levels.append(level)

    #plot line for each deck level
    deck_level_A = alt.Chart(deck_levels[0]).mark_line().encode(
        alt.X('x:Q'),
        alt.Y('y:Q')
    )
    deck_level_B = alt.Chart(deck_levels[1]).mark_line().encode(
        alt.X('x:Q'),
        alt.Y('y:Q')
    )
    deck_level_C = alt.Chart(deck_levels[2]).mark_line().encode(
        alt.X('x:Q'),
        alt.Y('y:Q')
    )
    deck_level_D = alt.Chart(deck_levels[3]).mark_line().encode(
        alt.X('x:Q'),
        alt.Y('y:Q')
    )
    deck_level_E = alt.Chart(deck_levels[4]).mark_line().encode(
        alt.X('x:Q'),
        alt.Y('y:Q')
    )
    deck_level_F = alt.Chart(deck_levels[5]).mark_line().encode(
        alt.X('x:Q'),
        alt.Y('y:Q')
    )
    deck_level_G = alt.Chart(deck_levels[6]).mark_line().encode(
        alt.X('x:Q'),
        alt.Y('y:Q')
    )

    #combine outline, line for each level, annotations and highlight desired level
    chart = (deck_legend_outline + deck_level_A + deck_level_B + deck_level_C + deck_level_D + \
             deck_level_E + deck_level_F + deck_level_G + points + current_level + text
            ).properties(width = 200, height = 300
            ).configure_axis(grid=False, titleFontSize=0, labelColor = "white", tickColor = "white"
            ).configure_title(fontSize = 20
            )
    
    return chart