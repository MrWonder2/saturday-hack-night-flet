import random


def get_random_male_first_name(descent):
    male_first_names = {
        'Italian': ['Marco', 'Luca', 'Alessio', 'Giovanni', 'Matteo', 'Antonio', 'Lorenzo', 'Davide', 'Fabio', 'Enzo'],
        'English': ['William', 'James', 'Benjamin', 'Samuel', 'Henry', 'Daniel', 'Charles', 'Thomas', 'Matthew', 'Robert'],
        'French': ['Olivier', 'Louis', 'Pierre', 'Antoine', 'Étienne', 'Alexandre', 'Luc', 'Paul', 'Gabriel', 'Théo'],
        'German': ['Maximilian', 'Friedrich', 'Heinrich', 'Wolfgang', 'Matthias', 'Sebastian', 'Julius', 'Leon', 'Hannes', 'Jonas'],
        'Russian': ['Alexei', 'Dmitry', 'Nikita', 'Ivan', 'Mikhail', 'Sergei', 'Andrei', 'Vladimir', 'Nikolai', 'Pavel'],
        'Indian': ['Ravi', 'Amit', 'Vikram', 'Rajesh', 'Arun', 'Kiran', 'Sanjay', 'Amitabh', 'Rahul', 'Ramesh']
    }
    return random.choice(male_first_names.get(descent, []))


def get_random_male_last_name(descent):
    male_last_names = {
        'Italian': ['Rossi', 'Conti', 'Moretti', 'Rizzo', 'Caruso', 'Ricci', 'Santoro', 'Pellegrini', 'Ferrari', 'Mancini'],
        'English': ['Smith', 'Johnson', 'Brown', 'Wilson', 'Davis', 'Anderson', 'Harris', 'Martin', 'Thompson', 'Robinson'],
        'French': ['Dupont', 'Lambert', 'Dubois', 'Martin', 'Lefebvre', 'Roy', 'Leroux', 'Girard', 'Simon', 'Boucher'],
        'German': ['Schmidt', 'Müller', 'Wagner', 'Becker', 'Fischer', 'Weber', 'Schulz', 'Hoffmann', 'Keller', 'Schneider'],
        'Russian': ['Ivanov', 'Petrov', 'Kuznetsov', 'Smirnov', 'Volkov', 'Sokolov', 'Orlov', 'Kozlov', 'Popov', 'Mikhailov'],
        'Indian': ['Patel', 'Shah', 'Gupta', 'Verma', 'Singh', 'Joshi', 'Mehra', 'Malik', 'Gandhi', 'Yadav']
    }
    return random.choice(male_last_names.get(descent, []))


def get_random_female_first_name(descent):
    female_first_names = {
        'Italian': ['Sofia', 'Isabella', 'Chiara', 'Elena', 'Valentina', 'Alessia', 'Ginevra', 'Livia', 'Bianca', 'Noemi'],
        'English': ['Emily', 'Olivia', 'Charlotte', 'Amelia', 'Lily', 'Sophia', 'Grace', 'Ella', 'Hannah', 'Madison'],
        'French': ['Camille', 'Elise', 'Margot', 'Manon', 'Sylvie', 'Élise', 'Juliette', 'Céline', 'Amélie', 'Nathalie'],
        'German': ['Emma', 'Lena', 'Johanna', 'Laura', 'Sophia', 'Hannah', 'Lea', 'Mia', 'Emilia', 'Julia'],
        'Russian': ['Anastasia', 'Yelena', 'Tatiana', 'Natalia', 'Ekaterina', 'Svetlana', 'Nina', 'Anna', 'Elena', 'Maria'],
        'Indian': ['Priya', 'Neha', 'Kavita', 'Anjali', 'Meera', 'Sakshi', 'Naina', 'Pooja', 'Sneha', 'Swati']
    }
    return random.choice(female_first_names.get(descent, []))


def get_random_female_last_name(descent):
    female_last_names = {
        'Italian': ['Romano', 'Esposito', 'De Luca', 'Rinaldi', 'Barbieri', 'Greco', 'Vitale', 'Russo', 'Mancini', 'Marino'],
        'English': ['Smith', 'Johnson', 'Brown', 'Wilson', 'Davis', 'Taylor', 'Evans', 'Scott', 'Allen', 'Bennett'],
        'French': ['Dubois', 'Martin', 'Lambert', 'Moreau', 'Bernard', 'Petit', 'Dufresne', 'Leroy', 'Lefevre', 'Rousseau'],
        'German': ['Müller', 'Schmidt', 'Becker', 'Weber', 'Fischer', 'Schulz', 'Hoffmann', 'Keller', 'Wagner', 'Hermann'],
        'Russian': ['Ivanova', 'Petrova', 'Kuznetsova', 'Smirnova', 'Volkova', 'Sokolova', 'Orlova', 'Kozlova', 'Popova', 'Mikhailova'],
        'Indian': ['Patel', 'Shah', 'Gupta', 'Verma', 'Singh', 'Yadav', 'Mishra', 'Garg', 'Saxena', 'Choudhary']
    }
    return random.choice(female_last_names.get(descent, []))


def get_random_unisex_first_name(descent):
    unisex_first_names = {
        'Italian': ['Alessio', 'Valentina', 'Luca', 'Michele', 'Simona', 'Andrea', 'Claudia', 'Davide', 'Elisa', 'Fabrizio'],
        'English': ['Jordan', 'Taylor', 'Riley', 'Morgan', 'Casey', 'Avery', 'Alex', 'Blake', 'Peyton', 'Reese'],
        'French': ['Morgan', 'Camille', 'Sylvie', 'Robin', 'Jules', 'Aubrey', 'Cameron', 'Maxime', 'Quinn', 'Elliott'],
        'German': ['Johanna', 'Sophia', 'Lena', 'Andrea', 'Robin', 'Marian', 'Julia', 'Sascha', 'Dominik', 'Kim'],
        'Russian': ['Nikita', 'Ekaterina', 'Yelena', 'Sasha', 'Dima', 'Alex', 'Misha', 'Kira', 'Artyom', 'Nastya'],
        'Indian': ['Surya', 'Ragini', 'Kiran', 'Amit', 'Raj', 'Pooja', 'Ravi', 'Simran', 'Sahil', 'Neha']
    }
    return random.choice(unisex_first_names.get(descent, []))


def get_random_unisex_last_name(descent):
    unisex_last_names = {
        'Italian': ['Rossi', 'Conti', 'Moretti', 'Bianchi', 'Ferrari', 'Russo', 'Mancini', 'Marchetti', 'Ricci', 'Santoro'],
        'English': ['Taylor', 'Jordan', 'Morgan', 'Casey', 'Avery', 'Alex', 'Riley', 'Reese', 'Bailey', 'Gray'],
        'French': ['Lambert', 'Dubois', 'Martin', 'Robin', 'Jules', 'Cameron', 'Maxime', 'Blanc', 'Leroux', 'Renard'],
        'German': ['Schmidt', 'Müller', 'Becker', 'Weber', 'Fischer', 'Schulz', 'Hoffmann', 'Keller', 'Wagner', 'Hermann'],
        'Russian': ['Ivanov', 'Petrov', 'Kuznetsov', 'Smirnov', 'Volkov', 'Sokolov', 'Orlov', 'Kozlov', 'Popov', 'Mikhailov'],
        'Indian': ['Patel', 'Shah', 'Gupta', 'Verma', 'Singh', 'Joshi', 'Mehra', 'Malik', 'Gandhi', 'Yadav']
    }
    return random.choice(unisex_last_names.get(descent, []))
