import streamlit as st

# Default recipe data
default_recipe = {
    "Flour": 768,
    "Sugar": 383,
    "Oil": 237,
    "Coco Powder": 116,
    "Baking Powder": 15,
    "Water / Milk": 387,
    "Output Qty": 216
}

def calculate_cookies(ingredients):
    """
    Calculate the number of cookies that can be made based on the input ingredients.
    """
    total_grams = sum([v for k, v in ingredients.items() if k != "Output Qty"])
    return round(total_grams / default_recipe["Flour"] * default_recipe["Output Qty"])

st.title("Cookie Recipe Calculator")

# Display default recipe
st.subheader("Default Recipe:")
for ingredient, amount in default_recipe.items():
    st.text(f"{ingredient}: {amount} g")

# User input for ingredients
input_ingredients = {}
for ingredient in default_recipe.keys():
    if ingredient == "Output Qty":
        continue
    amount = st.number_input(f"{ingredient} (g)", value=default_recipe[ingredient])
    input_ingredients[ingredient] = amount

# Calculate and display the result
output_qty = calculate_cookies(input_ingredients)
st.header(f"You can make approximately {output_qty} cookies.")