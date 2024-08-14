import pandas as pd

df = pd.read_pickle('../../data/social_explorer_processed/terrain_dataset.pkl')

df = df.query('Year >= 2011').reset_index(drop=True)

# Function to create summary sentences
def summarize_row(row):
    summary = (
        f"{row['County']} in {row['State']} has the following terrain makeup: "
        f"{row['% Open Water']}% open water, "
        f"{row['% Perennial Ice/Snow']}% perennial ice/snow, "
        f"{row['% Developed, Open Space']}% developed open space, "
        f"{row['% Developed, Low Intensity']}% developed low intensity, "
        f"{row['% Developed, Medium Intensity']}% developed medium intensity, "
        f"{row['% Developed, High Intensity']}% developed high intensity, "
        f"{row['% Barren Land (Rock/Sand/Clay)']}% barren land (rock/sand/clay), "
        f"{row['% Deciduous Forest']}% deciduous forest, "
        f"{row['% Evergreen Forest']}% evergreen forest, "
        f"{row['% Mixed Forest']}% mixed forest, "
        f"{row['% Shrub/Scrub']}% shrub/scrub, "
        f"{row['% Grassland/Herbaceous']}% grassland/herbaceous, "
        f"{row['% Pasture/Hay']}% pasture/hay, "
        f"{row['% Cultivated Crops']}% cultivated crops, "
        f"{row['% Woody Wetlands']}% woody wetlands, "
        f"{row['% Emergent Herbaceous Wetlands']}% emergent herbaceous wetlands, "
        f"{row['Farmland']}% farmland, "
        f"{row['Houses with lots of land']}% houses with lots of land, "
        f"{row['Suburbia']}% suburbia, "
        f"{row['Big city']}% big city, "
        f"{row['Forests']}% forests, "
        f"{row['Open fields']}% open fields, "
        f"{row['Wetlands']}% wetlands, "
        f"{row['Open water']}% open water, "
        f"{row['Rock/Sand/Clay']}% rock/sand/clay, "
        f"{row['Perennial ice/snow']}% perennial ice/snow."
    )
    return summary

# Function to create the combined string
def create_combined_string(row):
    question = f"What are the key terrain characteristics of {row['County']}?"
    answer = summarize_row(row)
    return f"[INST] {question} [/INST] {answer} </s>"

# Apply the function to each row and create the new column
df['Combined'] = df.apply(create_combined_string, axis=1)

# Create a new DataFrame with the combined column
combined_df = df[['Combined']]

combined_df.to_pickle('../data/social_explorer/combined_df.pkl')

# Display the new DataFrame
print(combined_df.iloc[0]['Combined'])
