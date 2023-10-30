import turtle
import pandas

screen = turtle.Turtle()

screen = turtle.Screen()
screen.title("Guess The Name Of The African Country")
image = "african_map.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("african_countries.csv")

guessed_country = []
score =0
all_countries = data.Country.to_list()
print(all_countries)

while len(guessed_country) < 55:
    answer=(screen.textinput(title=f"{len(guessed_country)}/{len(all_countries)}", prompt="Guess the name of any other country you know: ")).title()
    
    if answer == "exit":
        missing_countries =[country for country in all_countries if country not in guessed_country ]
        new_data = pandas.DataFrame(missing_countries)
        new_data.to_csv("countries_to_learn.csv")
        break

    # is_present = answer in data["Country"].values
    # if is_present:
    #     index_position = all_countries.index(answer)
    #     pos_x = data["x"][index_position]
    #     pos_y = data["y"][index_position]   

# The above code works similarly to the one below

    if answer in all_countries:
        guessed_country.append(answer)
        country_data = data[data.Country == answer]
        pos_x = country_data.x
        pos_y = country_data.y
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(pos_x), int(pos_y))
        t.write(answer)
        score+=1



screen.exitonclick()