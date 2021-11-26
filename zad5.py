import requests
import unittest

class Meal:

    def get_meal_by_id(self, id):
        if type(id) is int:
            response = requests.get(f"https://www.themealdb.com/api/json/v1/1/lookup.php?i={id}")
            if response.json()['meals'] == None:
                return "Brak potrawy o tym id."
            else:
                result = response.json()['meals'][0]['strMeal']
                return result
        else:
            raise TypeError("error")

    def get_meals_by_first_letter(self, letter):
        letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTEUVWXYZ"
        meals = []
        if type(letter) is str and letter in letters:
            response = requests.get(f"https://www.themealdb.com/api/json/v1/1/search.php?f={letter}")
            if response.json()['meals'] == None:
                return "Brak potraw na ta litere."
            else:
                result = response.json()['meals']
                for i in result:
                    meals.append(i['strMeal'])
                return meals
        else:
            raise TypeError("error")

    def get_vegetarian_meals(self):
        meals = []
        response = requests.get("https://www.themealdb.com/api/json/v1/1/filter.php?c=vegetarian")
        result = response.json()['meals']
        for i in result:
            meals.append(i['strMeal'])
        return meals

    def get_meal_by_category(self, category):
        categories = ['Beef', 'Breakfast', 'Chicken', 'Dessert', 'Goat', 'Lamb', 'Miscellaneous', 'Pasta', 'Pork', 'Seafood', 'Side', 'Starter', 'Vegan', 'Vegetarian']
        meals = []
        if type(category) is str and category in categories:
            response = requests.get(f"https://www.themealdb.com/api/json/v1/1/filter.php?c={category}")
            if response.json()['meals'] == None:
                return "Brak potraw z tej kategorii."
            else:
                result = response.json()['meals']
                for i in result:
                    meals.append(i['strMeal'])
                return meals
        else:
            raise TypeError("error")


class Recipes:

    def get_recipe_by_id(self, id):
        recipe = {}
        if type(id) is int:
            response = requests.get(f"https://www.themealdb.com/api/json/v1/1/lookup.php?i={id}")
            if response.json()['meals'] == None:
                return "Brak potrawy/przepisu o tym id."
            else:
                result = response.json()['meals'][0]
                recipe[result['strMeal']] = result['strInstructions']
                return recipe
        else:
            raise TypeError("error")

    def get_recipe_by_name(self, name):
        recipes = []
        if type(name) is str:
            response = requests.get(f"https://www.themealdb.com/api/json/v1/1/search.php?s={name}")
            if response.json()['meals'] == None:
                return "Brak potrawy/przepisu o takiej nazwie."
            else:
                result = response.json()['meals']
                for i in result:
                    recipe = {}
                    recipe[i['strMeal']] = i['strInstructions']
                    recipes.append(recipe)
                return recipes
        else:
            raise TypeError("error")

class Ingridients:

    def get_recipe_ingr(self, id):
        ingredients = []
        if type(id) is int:
            response = requests.get(f"https://www.themealdb.com/api/json/v1/1/lookup.php?i={id}")
            if response.json()['meals'] == None:
                return "Brak potrawy o takim id."
            else:
                result = response.json()['meals'][0]
                for i in range(1, 21):
                    ingredients.append(result[f'strIngredient{i}'])
                return ingredients
        else:
            raise TypeError("error")


class Categories:

    def list_all_categories(self):
        categories = []
        response = requests.get("https://www.themealdb.com/api/json/v1/1/list.php?c=list")
        result = response.json()['meals']
        for i in result:
            categories.append(i['strCategory'])
        return categories

class Area:

    def list_all_area(self):
        area = []
        response = requests.get("https://www.themealdb.com/api/json/v1/1/list.php?a=list")
        result = response.json()['meals']
        for i in result:
            area.append(i['strArea'])
        return area


m = Meal()
r = Recipes()
i = Ingridients()
c = Categories()
a = Area()


class Test_food(unittest.TestCase):

    def test_meal_id_pos(self):
        self.assertEqual("Teriyaki Chicken Casserole", m.get_meal_by_id(52772))

    def test_meal_id_pos_empty(self):
        self.assertEqual("Brak potrawy o tym id.", m.get_meal_by_id(1))

    def test_meal_id_err_str(self):
        self.assertRaises(TypeError, m.get_meal_by_id, "a")

    def test_meal_id_err_float(self):
        self.assertRaises(TypeError, m.get_meal_by_id, 2.5)

    def test_meal_id_err_tup(self):
        self.assertRaises(TypeError, m.get_meal_by_id, ())

    def test_meal_id_err_arr(self):
        self.assertRaises(TypeError, m.get_meal_by_id, [])

    def test_meal_id_err_dict(self):
        self.assertRaises(TypeError, m.get_meal_by_id, {})

    def test_meal_id_err_bool(self):
        self.assertRaises(TypeError, m.get_meal_by_id, False)

    def test_meal_id_err_none(self):
        self.assertRaises(TypeError, m.get_meal_by_id, None)

    def test_meal_letter_pos(self):
        self.assertEqual(['Apple Frangipan Tart', 'Apple & Blackberry Crumble', 'Apam balik', 'Ayam Percik'], m.get_meals_by_first_letter("a"))

    def test_meal_letter_pos_empty(self):
        self.assertEqual("Brak potraw na ta litere.", m.get_meals_by_first_letter("x"))

    def test_meal_letter_err_str(self):
        self.assertRaises(TypeError, m.get_meals_by_first_letter, "aaa")

    def test_meal_letter_str_nonlett(self):
        self.assertRaises(TypeError, m.get_meals_by_first_letter, "1")

    def test_meal_letter_err_int(self):
        self.assertRaises(TypeError, m.get_meals_by_first_letter, 1)

    def test_meal_letter_err_float(self):
        self.assertRaises(TypeError, m.get_meals_by_first_letter, 2.5)

    def test_meal_letter_err_tup(self):
        self.assertRaises(TypeError, m.get_meals_by_first_letter, ())

    def test_meal_letter_err_arr(self):
        self.assertRaises(TypeError, m.get_meals_by_first_letter, [])

    def test_meal_letter_err_dict(self):
        self.assertRaises(TypeError, m.get_meals_by_first_letter, {})

    def test_meal_letter_err_bool(self):
        self.assertRaises(TypeError, m.get_meals_by_first_letter, False)

    def test_meal_letter_err_none(self):
        self.assertRaises(TypeError, m.get_meals_by_first_letter, None)

    def test_meal_cat_pos(self):
        self.assertEqual(['Baked salmon with fennel & tomatoes', 'Cajun spiced fish tacos', 'Escovitch Fish', 'Fish fofos', 'Fish pie', 'Fish Stew with Rouille', 'Garides Saganaki', 'Grilled Portuguese sardines', 'Honey Teriyaki Salmon', 'Kedgeree', 'Kung Po Prawns', 'Laksa King Prawn Noodles', 'Mediterranean Pasta Salad', 'Mee goreng mamak', 'Nasi lemak', 'Portuguese fish stew (Caldeirada de peixe)', 'Recheado Masala Fish', 'Salmon Avocado Salad', 'Salmon Prawn Risotto', 'Saltfish and Ackee', 'Seafood fideuà', 'Shrimp Chow Fun', 'Sledz w Oleju (Polish Herrings)', 'Spring onion and prawn empanadas', 'Three Fish Pie', 'Tuna and Egg Briks', 'Tuna Nicoise'], m.get_meal_by_category("Seafood"))

    def test_meal_cat_err_str(self):
        self.assertRaises(TypeError, m.get_meal_by_category, "aaa")

    def test_meal_cat_str_nonlett(self):
        self.assertRaises(TypeError, m.get_meal_by_category, "1")

    def test_meal_cat_err_int(self):
        self.assertRaises(TypeError, m.get_meal_by_category, 1)

    def test_meal_cat_err_float(self):
        self.assertRaises(TypeError, m.get_meal_by_category, 2.5)

    def test_meal_cat_err_tup(self):
        self.assertRaises(TypeError, m.get_meal_by_category, ())

    def test_meal_cat_err_arr(self):
        self.assertRaises(TypeError, m.get_meal_by_category, [])

    def test_meal_cat_err_dict(self):
        self.assertRaises(TypeError, m.get_meal_by_category, {})

    def test_meal_cat_err_bool(self):
        self.assertRaises(TypeError, m.get_meal_by_category, False)

    def test_meal_cat_err_none(self):
        self.assertRaises(TypeError, m.get_meal_by_category, None)

    def test_recipe_id_pos(self):
        self.assertEqual({'Teriyaki Chicken Casserole': 'Preheat oven to 350° F. Spray a 9x13-inch baking pan with non-stick spray.\r\nCombine soy sauce, ½ cup water, brown sugar, ginger and garlic in a small saucepan and cover. Bring to a boil over medium heat. Remove lid and cook for one minute once boiling.\r\nMeanwhile, stir together the corn starch and 2 tablespoons of water in a separate dish until smooth. Once sauce is boiling, add mixture to the saucepan and stir to combine. Cook until the sauce starts to thicken then remove from heat.\r\nPlace the chicken breasts in the prepared pan. Pour one cup of the sauce over top of chicken. Place chicken in oven and bake 35 minutes or until cooked through. Remove from oven and shred chicken in the dish using two forks.\r\n*Meanwhile, steam or cook the vegetables according to package directions.\r\nAdd the cooked vegetables and rice to the casserole dish with the chicken. Add most of the remaining sauce, reserving a bit to drizzle over the top when serving. Gently toss everything together in the casserole dish until combined. Return to oven and cook 15 minutes. Remove from oven and let stand 5 minutes before serving. Drizzle each serving with remaining sauce. Enjoy!'}, r.get_recipe_by_id(52772))

    def test_recipe_id_pos_empty(self):
        self.assertEqual("Brak potrawy/przepisu o tym id.", r.get_recipe_by_id(1))

    def test_recipe_id_err_str(self):
        self.assertRaises(TypeError, r.get_recipe_by_id, "a")

    def test_recipe_id_err_float(self):
        self.assertRaises(TypeError, r.get_recipe_by_id, 2.5)

    def test_recipe_id_err_tup(self):
        self.assertRaises(TypeError, r.get_recipe_by_id, ())

    def test_recipe_id_err_arr(self):
        self.assertRaises(TypeError, r.get_recipe_by_id, [])

    def test_recipe_id_err_dict(self):
        self.assertRaises(TypeError, r.get_recipe_by_id, {})

    def test_recipe_id_err_bool(self):
        self.assertRaises(TypeError, r.get_recipe_by_id, False)

    def test_recipe_id_err_none(self):
        self.assertRaises(TypeError, r.get_recipe_by_id, None)

    def test_recipe_letter_pos(self):
        self.assertEqual([{'Chicken Handi': 'Take a large pot or wok, big enough to cook all the chicken, and heat the oil in it. Once the oil is hot, add sliced onion and fry them until deep golden brown. Then take them out on a plate and set aside.\r\nTo the same pot, add the chopped garlic and sauté for a minute. Then add the chopped tomatoes and cook until tomatoes turn soft. This would take about 5 minutes.\r\nThen return the fried onion to the pot and stir. Add ginger paste and sauté well.\r\nNow add the cumin seeds, half of the coriander seeds and chopped green chillies. Give them a quick stir.\r\nNext goes in the spices – turmeric powder and red chilli powder. Sauté the spices well for couple of minutes.\r\nAdd the chicken pieces to the wok, season it with salt to taste and cook the chicken covered on medium-low heat until the chicken is almost cooked through. This would take about 15 minutes. Slowly sautéing the chicken will enhance the flavor, so do not expedite this step by putting it on high heat.\r\nWhen the oil separates from the spices, add the beaten yogurt keeping the heat on lowest so that the yogurt doesn’t split. Sprinkle the remaining coriander seeds and add half of the dried fenugreek leaves. Mix well.\r\nFinally add the cream and give a final mix to combine everything well.\r\nSprinkle the remaining kasuri methi and garam masala and serve the chicken handi hot with naan or rotis. Enjoy!'}, {'Chicken Congee': 'STEP 1 - MARINATING THE CHICKEN\r\nIn a bowl, add chicken, salt, white pepper, ginger juice and then mix it together well.\r\nSet the chicken aside.\r\nSTEP 2 - RINSE THE WHITE RICE\r\nRinse the rice in a metal bowl or pot a couple times and then drain the water.\r\nSTEP 2 - BOILING THE WHITE RICE\r\nNext add 8 cups of water and then set the stove on high heat until it is boiling. Once rice porridge starts to boil, set the stove on low heat and then stir it once every 8-10 minutes for around 20-25 minutes.\r\nAfter 25 minutes, this is optional but you can add a little bit more water to make rice porridge to make it less thick or to your preference.\r\nNext add the marinated chicken to the rice porridge and leave the stove on low heat for another 10 minutes.\r\nAfter an additional 10 minutes add the green onions, sliced ginger, 1 pinch of salt, 1 pinch of white pepper and stir for 10 seconds.\r\nServe the rice porridge in a bowl\r\nOptional: add Coriander on top of the rice porridge.'}, {'Chicken Karaage': "Add the ginger, garlic, soy sauce, sake and sugar to a bowl and whisk to combine. Add the chicken, then stir to coat evenly. Cover and refrigerate for at least 1 hour.\r\n\r\nAdd 1 inch of vegetable oil to a heavy bottomed pot and heat until the oil reaches 360 degrees F. Line a wire rack with 2 sheets of paper towels and get your tongs out. Put the potato starch in a bowl\r\n\r\nAdd a handful of chicken to the potato starch and toss to coat each piece evenly.\r\n\r\nFry the karaage in batches until the exterior is a medium brown and the chicken is cooked through. Transfer the fried chicken to the paper towel lined rack. If you want the karaage to stay crispy longer, you can fry the chicken a second time, until it's a darker color after it's cooled off once. Serve with lemon wedges."}, {'Chicken Marengo': 'Heat the oil in a large flameproof casserole dish and stir-fry the mushrooms until they start to soften. Add the chicken legs and cook briefly on each side to colour them a little.\r\nPour in the passata, crumble in the stock cube and stir in the olives. Season with black pepper – you shouldn’t need salt. Cover and simmer for 40 mins until the chicken is tender. Sprinkle with parsley and serve with pasta and a salad, or mash and green veg, if you like.'}, {'Tandoori chicken': 'Mix the lemon juice with the paprika and red onions in a large shallow dish. Slash each chicken thigh three times, then turn them in the juice and set aside for 10 mins.\r\nMix all of the marinade ingredients together and pour over the chicken. Give everything a good mix, then cover and chill for at least 1 hr. This can be done up to a day in advance.\r\nHeat the grill. Lift the chicken pieces onto a rack over a baking tray. Brush over a little oil and grill for 8 mins on each side or until lightly charred and completely cooked through.'}, {'Chicken Couscous': 'Heat the olive oil in a large frying pan and cook the onion for 1-2 mins just until softened. Add the chicken and fry for 7-10 mins until cooked through and the onions have turned golden. Grate over the ginger, stir through the harissa to coat everything and cook for 1 min more.\r\n\r\nTip in the apricots, chickpeas and couscous, then pour over the stock and stir once. Cover with a lid or tightly cover the pan with foil and leave for about 5 mins until the couscous has soaked up all the stock and is soft. Fluff up the couscous with a fork and scatter over the coriander to serve. Serve with extra harissa, if you like.'}, {'Kung Pao Chicken': 'Combine the sake or rice wine, soy sauce, sesame oil and cornflour dissolved in water. Divide mixture in half.\r\nIn a glass dish or bowl, combine half of the sake mixture with the chicken pieces and toss to coat. Cover dish and place in refrigerator for about 30 minutes.\r\nIn a medium frying pan, combine remaining sake mixture, chillies, vinegar and sugar. Mix together and add spring onion, garlic, water chestnuts and peanuts. Heat sauce slowly over medium heat until aromatic.\r\nMeanwhile, remove chicken from marinade and sauté in a large frying pan until juices run clear. When sauce is aromatic, add sautéed chicken and let simmer together until sauce thickens.'}, {'Chicken Basquaise': "Preheat the oven to 180°C/Gas mark 4. Have the chicken joints ready to cook. Heat the butter and 3 tbsp olive oil in a flameproof casserole or large frying pan. Brown the chicken pieces in batches on both sides, seasoning them with salt and pepper as you go. Don't crowd the pan - fry the chicken in small batches, removing the pieces to kitchen paper as they are done.\r\n\r\nAdd a little more olive oil to the casserole and fry the onions over a medium heat for 10 minutes, stirring frequently, until softened but not browned. Add the rest of the oil, then the peppers and cook for another 5 minutes.\r\n\r\nAdd the chorizo, sun-dried tomatoes and garlic and cook for 2-3 minutes. Add the rice, stirring to ensure it is well coated in the oil. Stir in the tomato paste, paprika, bay leaves and chopped thyme. Pour in the stock and wine. When the liquid starts to bubble, turn the heat down to a gentle simmer. Press the rice down into the liquid if it isn't already submerged and place the chicken on top. Add the lemon wedges and olives around the chicken.\r\n\r\nCover and cook in the oven for 50 minutes. The rice should be cooked but still have some bite, and the chicken should have juices that run clear when pierced in the thickest part with a knife. If not, cook for another 5 minutes and check again."}, {'Chicken Parmentier': 'For the topping, boil the potatoes in salted water until tender. Drain and push through a potato ricer, or mash thoroughly. Stir in the butter, cream and egg yolks. Season and set aside.\r\nFor the filling, melt the butter in a large pan. Add the shallots, carrots and celery and gently fry until soft, then add the garlic. Pour in the wine and cook for 1 minute. Stir in the tomato purée, chopped tomatoes and stock and cook for 10–15 minutes, until thickened. Add the shredded chicken, olives and parsley. Season to taste with salt and pepper.\r\nPreheat the oven to 180C/160C Fan/Gas 4.\r\nPut the filling in a 20x30cm/8x12in ovenproof dish and top with the mashed potato. Grate over the Gruyère. Bake for 30–35 minutes, until piping hot and the potato is golden-brown.'}, {'Brown Stew Chicken': 'Squeeze lime over chicken and rub well. Drain off excess lime juice.\r\nCombine tomato, scallion, onion, garlic, pepper, thyme, pimento and soy sauce in a large bowl with the chicken pieces. Cover and marinate at least one hour.\r\nHeat oil in a dutch pot or large saucepan. Shake off the seasonings as you remove each piece of chicken from the marinade. Reserve the marinade for sauce.\r\nLightly brown the chicken a few pieces at a time in very hot oil. Place browned chicken pieces on a plate to rest while you brown the remaining pieces.\r\nDrain off excess oil and return the chicken to the pan. Pour the marinade over the chicken and add the carrots. Stir and cook over medium heat for 10 minutes.\r\nMix flour and coconut milk and add to stew, stirring constantly. Turn heat down to minimum and cook another 20 minutes or until tender.'}, {'Katsu Chicken curry': 'Prep:15min  ›  Cook:30min  ›  Ready in:45min \r\n\r\nFor the curry sauce: Heat oil in medium non-stick saucepan, add onion and garlic and cook until softened. Stir in carrots and cook over low heat for 10 to 12 minutes.\r\nAdd flour and curry powder; cook for 1 minute. Gradually stir in stock until combined; add honey, soy sauce and bay leaf. Slowly bring to the boil.\r\nTurn down heat and simmer for 20 minutes or until sauce thickens but is still of pouring consistency. Stir in garam masala. Pour the curry sauce through a sieve; return to saucepan and keep on low heat until ready to serve.\r\nFor the chicken: Season both sides of chicken breasts with salt and pepper. Place flour, egg and breadcrumbs in separate bowls and arrange in a row. Coat the chicken breasts in flour, then dip them into the egg, then coat in breadcrumbs, making sure you cover both sides.\r\nHeat oil in large frying pan over medium-high heat. Place chicken into hot oil and cook until golden brown, about 3 or 4 minutes each side. Once cooked, place on kitchen paper to absorb excess oil.\r\nPour curry sauce over chicken, serve with white rice and enjoy!'}, {'Nutty Chicken Curry': 'Finely slice a quarter of the chilli, then put the rest in a food processor with the ginger, garlic, coriander stalks and one-third of the leaves. Whizz to a rough paste with a splash of water if needed.\r\nHeat the oil in a frying pan, then quickly brown the chicken chunks for 1 min. Stir in the paste for another min, then add the peanut butter, stock and yogurt. When the sauce is gently bubbling, cook for 10 mins until the chicken is just cooked through and sauce thickened. Stir in most of the remaining coriander, then scatter the rest on top with the chilli, if using. Eat with rice or mashed sweet potato.'}, {"General Tso's Chicken": "DIRECTIONS:\r\nSTEP 1 - SAUCE\r\nIn a bowl, add 2 Cups of water, 2 Tablespoon soy sauce, 2 Tablespoon white vinegar, sherry cooking wine, 1/4 Teaspoon white pepper, minced ginger, minced garlic, hot pepper, ketchup, hoisin sauce, and sugar.\r\nMix together well and set aside.\r\nSTEP 2 - MARINATING THE CHICKEN\r\nIn a bowl, add the chicken, 1 pinch of salt, 1 pinch of white pepper, 2 egg whites, and 3 Tablespoon of corn starch\r\nSTEP 3 - DEEP FRY THE CHICKEN\r\nDeep fry the chicken at 350 degrees for 3-4 minutes or until it is golden brown and loosen up the chicken so that they don't stick together.\r\nSet the chicken aside.\r\nSTEP 4 - STIR FRY\r\nAdd the sauce to the wok and then the broccoli and wait until it is boiling.\r\nTo thicken the sauce, whisk together 2 Tablespoon of cornstarch and 4 Tablespoon of water in a bowl and slowly add to your stir-fry until it's the right thickness.\r\nNext add in the chicken and stir-fry for a minute and serve on a plate"}, {'Kentucky Fried Chicken': 'Preheat fryer to 350°F. Thoroughly mix together all the spice mix ingredients.\r\nCombine spice mix with flour, brown sugar and salt.\r\nDip chicken pieces in egg white to lightly coat them, then transfer to flour mixture. Turn a few times and make sure the flour mix is really stuck to the chicken. Repeat with all the chicken pieces.\r\nLet chicken pieces rest for 5 minutes so crust has a chance to dry a bit.\r\nFry chicken in batches. Breasts and wings should take 12-14 minutes, and legs and thighs will need a few more minutes. Chicken pieces are done when a meat thermometer inserted into the thickest part reads 165°F.\r\nLet chicken drain on a few paper towels when it comes out of the fryer. Serve hot.'}, {'Chicken Ham and Leek Pie': 'Heat the chicken stock in a lidded saucepan. Add the chicken breast and bring to a low simmer. Cover with a lid and cook for 10 minutes. Remove the chicken breasts from the water with tongs and place on a plate. Pour the cooking liquor into a large jug.\r\nMelt 25g/1oz of the butter in a large heavy-based saucepan over a low heat. Stir in the leeks and fry gently for two minutes, stirring occasionally until just softened. Add the garlic and cook for a further minute. Add the remaining butter and stir in the flour as soon as the butter has melted. Cook for 30 seconds, stirring constantly.\r\nSlowly pour the milk into the pan, just a little at a time, stirring well between each adding. Gradually add 250ml/10fl oz of the reserved stock and the wine, if using, stirring until the sauce is smooth and thickened slightly. Bring to a gentle simmer and cook for 3 minutes.\r\nSeason the mixture, to taste, with salt and freshly ground black pepper. Remove from the heat and stir in the cream. Pour into a large bowl and cover the surface of the sauce with cling ilm to prevent a skin forming. Set aside to cool.\r\nPreheat the oven to 200C/400F/Gas 6. Put a baking tray in the oven to heat.\r\nFor the pastry, put the flour and butter in a food processor and blend on the pulse setting until the mixture resembles fine breadcrumbs. With the motor running, add the beaten egg and water and blend until the mixture forms a ball. Portion off 250g/10oz of pastry for the lid.\r\nRoll the remaining pastry out on a lightly floured surface, turning the pastry frequently until around 5mm/¼in thick and 4cm/1½in larger than the pie dish. Lift the pastry over the rolling pin and place it gently into the pie dish. Press the pastry firmly up the sides, making sure there are no air bubbles. Leave the excess pastry overhanging the sides.\r\nCut the chicken breasts into 3cm/1¼in pieces. Stir the chicken, ham and leeks into the cooled sauce. Pour the chicken filling into the pie dish. Brush the rim of the dish with beaten egg. Roll out the reserved pastry for the lid.\r\nCover the pie with the pastry lid and press the edges together firmly to seal. Trim any excess pastry.\r\nMake a small hole in the centre of the pie with the tip of a knife. Glaze the top of the pie with beaten egg. Bake on the preheated tray in the centre of the oven for 35-40 minutes or until the pie is golden-brown all over and the filling is piping hot.'}, {'Chicken Alfredo Primavera': 'Heat 1 tablespoon of butter and 2 tablespoons of olive oil in a large skillet over medium-high heat. Season both sides of each chicken breast with seasoned salt and a pinch of pepper. Add the chicken to the skillet and cook for 5-7 minutes on each side, or until cooked through.  While the chicken is cooking, bring a large pot of water to a boil. Season the boiling water with a few generous pinches of kosher salt. Add the pasta and give it a stir. Cook, stirring occasionally, until al dente, about 12 minutes. Reserve 1/2 cup of  pasta water before draining the pasta.  Remove the chicken from the pan and transfer it to a cutting board; allow it to rest. Turn the heat down to medium and dd the remaining 1 tablespoon of butter and olive oil to the same pan you used to cook the chicken. Add the veggies (minus the garlic) and red pepper flakes to the pan and stir to coat with the oil and butter (refrain from seasoning with salt until the veggies are finished browning). Cook, stirring often, until the veggies are tender, about 5 minutes. Add the garlic and a generous pinch of salt and pepper to the pan and cook for 1 minute.  Deglaze the pan with the white wine. Continue to cook until the wine has reduced by half, about 3 minutes. Stir in the milk, heavy cream, and reserved pasta water. Bring the mixture to a gentle boil and allow to simmer and reduce for 2-3 minutes. Turn off the heat and add the Parmesan cheese and cooked pasta. Season with salt and pepper to taste. Garnish with Parmesan cheese and chopped parsley, if desired. '}, {'Chicken & mushroom Hotpot': 'Heat oven to 200C/180C fan/gas 6. Put the butter in a medium-size saucepan and place over a medium heat. Add the onion and leave to cook for 5 mins, stirring occasionally. Add the mushrooms to the saucepan with the onions.\r\n\r\nOnce the onion and mushrooms are almost cooked, stir in the flour – this will make a thick paste called a roux. If you are using a stock cube, crumble the cube into the roux now and stir well. Put the roux over a low heat and stir continuously for 2 mins – this will cook the flour and stop the sauce from having a floury taste.\r\n\r\nTake the roux off the heat. Slowly add the fresh stock, if using, or pour in 500ml water if you’ve used a stock cube, stirring all the time. Once all the liquid has been added, season with pepper, a pinch of nutmeg and mustard powder. Put the saucepan back onto a medium heat and slowly bring it to the boil, stirring all the time. Once the sauce has thickened, place on a very low heat. Add the cooked chicken and vegetables to the sauce and stir well. Grease a medium-size ovenproof pie dish with a little butter and pour in the chicken and mushroom filling.\r\n\r\nCarefully lay the potatoes on top of the hot-pot filling, overlapping them slightly, almost like a pie top.\r\n\r\nBrush the potatoes with a little melted butter and cook in the oven for about 35 mins. The hot-pot is ready once the potatoes are cooked and golden brown.'}, {'Teriyaki Chicken Casserole': 'Preheat oven to 350° F. Spray a 9x13-inch baking pan with non-stick spray.\r\nCombine soy sauce, ½ cup water, brown sugar, ginger and garlic in a small saucepan and cover. Bring to a boil over medium heat. Remove lid and cook for one minute once boiling.\r\nMeanwhile, stir together the corn starch and 2 tablespoons of water in a separate dish until smooth. Once sauce is boiling, add mixture to the saucepan and stir to combine. Cook until the sauce starts to thicken then remove from heat.\r\nPlace the chicken breasts in the prepared pan. Pour one cup of the sauce over top of chicken. Place chicken in oven and bake 35 minutes or until cooked through. Remove from oven and shred chicken in the dish using two forks.\r\n*Meanwhile, steam or cook the vegetables according to package directions.\r\nAdd the cooked vegetables and rice to the casserole dish with the chicken. Add most of the remaining sauce, reserving a bit to drizzle over the top when serving. Gently toss everything together in the casserole dish until combined. Return to oven and cook 15 minutes. Remove from oven and let stand 5 minutes before serving. Drizzle each serving with remaining sauce. Enjoy!'}, {'Potato Gratin with Chicken': "15 minute potato gratin with chicken and bacon greens: a gratin always seems more effort and more indulgent than ordinary boiled or roasts, but it doesn't have to take 45mins, it's nice for a change and you can control the calorie content by going with full fat to low fat creme fraiche. (It's always tastes better full fat though obviously!) to serve 4: use 800g of potatoes, finely slice and boil in a pan for about 5-8 mins till firmish, not soft. Finely slice 3 onions and place in an oven dish with 2 tblsp of olive oil and 100ml of chicken stock. Cook till the onions are soft then drain the potatoes and pour onto the onions. Season and spoon over cream or creme fraiche till all is covered but not swimming. Grate Parmesan over the top then finish under the grill till nicely golden. serve with chicken and bacon, peas and spinach."}, {'Chicken Quinoa Greek Salad': 'Cook the quinoa following the pack instructions, then rinse in cold water and drain thoroughly.\r\n\r\nMeanwhile, mix the butter, chilli and garlic into a paste. Toss the chicken fillets in 2 tsp of the olive oil with some seasoning. Lay in a hot griddle pan and cook for 3-4 mins each side or until cooked through. Transfer to a plate, dot with the spicy butter and set aside to melt.\r\n\r\nNext, tip the tomatoes, olives, onion, feta and mint into a bowl. Toss in the cooked quinoa. Stir through the remaining olive oil, lemon juice and zest, and season well. Serve with the chicken fillets on top, drizzled with any buttery chicken juices.'}, {'Piri-piri chicken and slaw': 'STEP 1\r\n\r\nWhizz together all of the marinade ingredients in a small food processor. Rub the marinade onto the chicken and leave for 1 hour at room temperature.\r\n\r\nSTEP 2\r\n\r\nHeat the oven to 190C/fan 170C/gas 5. Put the chicken in a roasting tray and cook for 1 hour 20 minutes. Rest under loose foil for 20 minutes. While the chicken is resting, mix together the slaw ingredients and season. Serve the chicken with slaw, fries and condiments.'}, {'Chicken Enchilada Casserole': "Cut each chicken breast in about 3 pieces, so that it cooks faster and put it in a small pot. Pour Enchilada sauce over it and cook covered on low to medium heat until chicken is cooked through, about 20 minutes. No water is needed, the chicken will cook in the Enchilada sauce. Make sure you stir occasionally so that it doesn't stick to the bottom.\r\nRemove chicken from the pot and shred with two forks.\r\nPreheat oven to 375 F degrees.\r\nStart layering the casserole. Start with about ¼ cup of the leftover Enchilada sauce over the bottom of a baking dish. I used a longer baking dish, so that I can put 2 corn tortillas across. Place 2 tortillas on the bottom, top with ⅓ of the chicken and ⅓ of the remaining sauce. Sprinkle with ⅓ of the cheese and repeat starting with 2 more tortillas, then chicken, sauce, cheese. Repeat with last layer with the remaining ingredients, tortillas, chicken, sauce and cheese.\r\nBake for 20 to 30 minutes uncovered, until bubbly and cheese has melted and started to brown on top.\r\nServe warm."}, {'Chicken Fajita Mac and Cheese': 'Fry your onion, peppers and garlic in olive oil until nicely translucent. Make a well in your veg and add your chicken. Add your seasoning and salt. Allow to colour slightly.\r\nAdd your cream, stock and macaroni.\r\nCook on low for 20 minutes. Add your cheeses, stir to combine.\r\nTop with roasted peppers and parsley.'}, {'Crock Pot Chicken Baked Tacos': 'Put the uncooked chicken breasts in the crock pot. Pour the full bottle of salad dressing over the chicken. Sprinkle the rest of the ingredients over the top and mix them in a bit with a spoon.\r\nCover your crock pot with the lid and cook on high for 4 hours.\r\nRemove all the chicken breasts from the crock pot and let cool.\r\nShred the chicken breasts and move to a glass bowl.\r\nPour most of the liquid over the shredded chicken.\r\nFOR THE TACOS:\r\nMake the guacamole sauce by mixing the avocado and green salsa together. Pour the guacamole mixture through a strainer until smooth and transfer to a squeeze bottle. Cut the tip off the lid of the squeeze bottle to make the opening more wide if needed.\r\nMake the sour cream sauce by mixing the sour cream and milk together until you get a more liquid sour cream sauce. Transfer to a squeeze bottle.\r\nIn a 9x 13 glass baking dish, fill all 12+ tacos with a layer of refried beans, cooked chicken and shredded cheese.\r\nBake at 450 for 10-15 minutes just until the cheese is melted and bubbling.\r\nOut of the oven top all the tacos with the sliced grape tomaotes, jalapeno and cilantro.\r\nFinish with a drizzle of guacamole and sour cream.\r\nEnjoy!'}, {'Jerk chicken with rice & peas': 'To make the jerk marinade, combine all the ingredients in a food processor along with 1 tsp salt, and blend to a purée. If you’re having trouble getting it to blend, just keep turning off the blender, stirring the mixture, and trying again. Eventually it will start to blend up – don’t be tempted to add water, as you want a thick paste.\r\n\r\nTaste the jerk mixture for seasoning – it should taste pretty salty, but not unpleasantly, puckering salty. You can now throw in more chillies if it’s not spicy enough for you. If it tastes too salty and sour, try adding in a bit more brown sugar until the mixture tastes well balanced.\r\n\r\nMake a few slashes in the chicken thighs and pour the marinade over the meat, rubbing it into all the crevices. Cover and leave to marinate overnight in the fridge.\r\n\r\nIf you want to barbecue your chicken, get the coals burning 1 hr or so before you’re ready to cook. Authentic jerked meats are not exactly grilled as we think of grilling, but sort of smoke-grilled. To get a more authentic jerk experience, add some wood chips to your barbecue, and cook your chicken over slow, indirect heat for 30 mins. To cook in the oven, heat to 180C/160C fan/gas 4. Put the chicken pieces in a roasting tin with the lime halves and cook for 45 mins until tender and cooked through.\r\n\r\nWhile the chicken is cooking, prepare the rice & peas. Rinse the rice in plenty of cold water, then tip it into a large saucepan with all the remaining ingredients except the kidney beans. Season with salt, add 300ml cold water and set over a high heat. Once the rice begins to boil, turn it down to a medium heat, cover and cook for 10 mins.\r\n\r\nAdd the beans to the rice, then cover with a lid. Leave off the heat for 5 mins until all the liquid is absorbed. Squeeze the roasted lime over the chicken and serve with the rice & peas, and some hot sauce if you like it really spicy.'}], r.get_recipe_by_name("chicken"))

    def test_recipe_letter_pos_empty(self):
        self.assertEqual("Brak potrawy/przepisu o takiej nazwie.", r.get_recipe_by_name("aaa"))

    def test_recipe_letter_err_int(self):
        self.assertRaises(TypeError, r.get_recipe_by_name, 1)

    def test_recipe_letter_err_float(self):
        self.assertRaises(TypeError, r.get_recipe_by_name, 2.5)

    def test_recipe_letter_err_tup(self):
        self.assertRaises(TypeError, r.get_recipe_by_name, ())

    def test_recipe_letter_err_arr(self):
        self.assertRaises(TypeError, r.get_recipe_by_name, [])

    def test_recipe_letter_err_dict(self):
        self.assertRaises(TypeError, r.get_recipe_by_name, {})

    def test_recipe_letter_err_bool(self):
        self.assertRaises(TypeError, r.get_recipe_by_name, False)

    def test_recipe_letter_err_none(self):
        self.assertRaises(TypeError, r.get_recipe_by_name, None)

    def test_ingr_id_pos(self):
        self.assertEqual(['soy sauce', 'water', 'brown sugar', 'ground ginger', 'minced garlic', 'cornstarch', 'chicken breasts', 'stir-fry vegetables', 'brown rice', '', '', '', '', '', '', None, None, None, None, None], i.get_recipe_ingr(52772))

    def test_ingr_id_pos_empty(self):
        self.assertEqual("Brak potrawy o takim id.", i.get_recipe_ingr(1))

    def test_ingr_id_err_str(self):
        self.assertRaises(TypeError, i.get_recipe_ingr, "a")

    def test_ingr_id_err_float(self):
        self.assertRaises(TypeError, i.get_recipe_ingr, 2.5)

    def test_ingr_id_err_tup(self):
        self.assertRaises(TypeError, i.get_recipe_ingr, ())

    def test_ingr_id_err_arr(self):
        self.assertRaises(TypeError, i.get_recipe_ingr, [])

    def test_ingr_id_err_dict(self):
        self.assertRaises(TypeError, i.get_recipe_ingr, {})

    def test_ingr_id_err_bool(self):
        self.assertRaises(TypeError, i.get_recipe_ingr, False)

    def test_ingr_id_err_none(self):
        self.assertRaises(TypeError, i.get_recipe_ingr, None)


if __name__ == "__main__":
    unittest.main()