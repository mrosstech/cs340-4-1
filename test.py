import animals

animalCreate = {"1" : 10000, 
                "age_upon_outcome" : "200 years", 
                "animal_id" : "A999999", 
                "animal_type" : "Other", 
                "breed" : "Raccoon", 
                "color" : "Gray/Black", 
                "date_of_birth" : "2015-11-20", 
                "datetime" : "2017-11-21 08:20:00", 
                "monthyear" : "2017-11-21T08:20:00", 
                "name" : "Pickles", 
                "outcome_subtype" : "Suffering", 
                "outcome_type" : "Cured", 
                "sex_upon_outcome" : "Male", 
                "location_lat" : 30.3718926151062, 
                "location_long" : -97.4774272170111, 
                "age_upon_outcome_in_weeks" : 104.621031746032 }
animalRead = {"breed": "Raccoon"}
animalShelter = animals.AnimalShelter("aacuser", "MyNewPassword")
createResult = animalShelter.create(animalCreate)
readResult = animalShelter.read(animalRead)
print(createResult)
print(readResult)

