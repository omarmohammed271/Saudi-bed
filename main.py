import streamlit as st
import streamlit.components.v1 as components
import pandas as pd

st.set_page_config(layout="wide")

df = pd.read_excel('beds.xlsx')

# Group by REGION_ID, CLUSTER_ID, and CLUSTER_NAME, and count occupied and vacant beds  
occupancy_counts = df.groupby(['CITY_NAME', 'REGION_ID', 'CLUSTER_ID', 'CLUSTER_NAME', 'MAPPED_BED_STATUS_EN']).size().unstack(fill_value=0)  
# Calculate total occupied and vacant beds  
occupancy_counts['Total_Occupied'] = occupancy_counts.get('Occupied', 0)  
occupancy_counts['Total_Vacant'] = occupancy_counts.get('Vacant', 0)  

# Calculate occupancy rate  
occupancy_counts['Occupancy_Rate'] = occupancy_counts['Total_Occupied'] / (occupancy_counts['Total_Occupied'] + occupancy_counts['Total_Vacant'])  


occupancy_counts.reset_index(inplace=True)  

# Display the results  
cluster_data = occupancy_counts[['CITY_NAME', 'REGION_ID', 'CLUSTER_ID', 'CLUSTER_NAME', 'Total_Occupied', 'Total_Vacant', 'Occupancy_Rate']]
# st.write(cluster_data)



# Group by REGION_ID, CLUSTER_ID, and CLUSTER_NAME, and count occupied and vacant beds  
occupancy_counts = df.groupby(['CITY_NAME', 'FACILITY_NAME_EN', 'REGION_ID', 'CLUSTER_ID', 'CLUSTER_NAME', 'MAPPED_BED_STATUS_EN']).size().unstack(fill_value=0)  
# Calculate total occupied and vacant beds  
occupancy_counts['Total_Occupied'] = occupancy_counts.get('Occupied', 0)  
occupancy_counts['Total_Vacant'] = occupancy_counts.get('Vacant', 0)  

# Calculate occupancy rate  
occupancy_counts['Occupancy_Rate'] = occupancy_counts['Total_Occupied'] / (occupancy_counts['Total_Occupied'] + occupancy_counts['Total_Vacant'])  


occupancy_counts.reset_index(inplace=True)  

# Display the results  
facility_data = occupancy_counts[['CITY_NAME', 'FACILITY_NAME_EN', 'REGION_ID', 'CLUSTER_ID', 'CLUSTER_NAME', 'Total_Occupied', 'Total_Vacant', 'Occupancy_Rate']]
# st.write(facility_data)

styling = """

<link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
<style>

    /* For WebKit browsers (Chrome, Safari) */
    ::-webkit-scrollbar {
        width: 12px; /* Width of the scrollbar */
    }

    ::-webkit-scrollbar-track {
        background: #2c2c2c; /* Background of the scrollbar track */
        border-radius: 10px; /* Rounded corners for the track */
    }

    ::-webkit-scrollbar-thumb {
        background: #747474FF; /* Color of the scrollbar thumb */
        border-radius: 10px; /* Rounded corners for the thumb */
    }

    ::-webkit-scrollbar-thumb:hover {
        background: #747474FF; /* Color of the scrollbar thumb on hover */
    }

    /* For Firefox */
    * {
        scrollbar-width: thin; /* Use a thin scrollbar */
        scrollbar-color: #747474FF #2c2c2c; /* Thumb color and track color */
    }

    /* For Edge (also WebKit based) */
    ::-ms-scrollbar {
        width: 12px;
        background: #747474FF;
        border-radius: 10px;
    }

    ::-ms-scrollbar-thumb {
        background: #2c2c2c;
        border-radius: 10px;
    }

    ::-ms-scrollbar-thumb:hover {
        background: #747474FF;
    }
    
    /* 1. Standard Laptop Screens (1024px - 1440px) */
    @media (max-width: 1440px) {
        
        /* Define the fade-in/fade-out animation */
        @keyframes fadeInOut {
        0% {
            opacity: 0; /* Fully transparent */
            background-position: 0% 50%; /* Start gradient at 0% */
        }
        50% {
            opacity: 1; /* Fully visible */
            background-position: 100% 50%; /* Move gradient to 100% */
        }
        100% {
            opacity: 0; /* Fade out to fully transparent */
            background-position: 0% 50%; /* Back to starting position */
        }
        }

        /* Apply gradient and animation to the text */
        .fade-animation {
        display: inline-block;
        color: orange;
        animation: fadeInOut 4s ease-in-out infinite; /* Duration and infinite loop */
        background-size: 200% auto; /* Ensures smooth gradient transition */
        }

        /* Style for the growing, disappearing circle (background) */
        .marker-animation {
            fill: none;
            stroke: rgba(255, 0, 0, 0.5);  /* Red color with opacity */
            stroke-width: 2;
            animation: grow 2s ease-out infinite;
            transition: all 0.2s;
        }

        /* Keyframe for the growing animation (behind the dot) */
        @keyframes grow {
            0% {
                r: 5;
                opacity: 0.7;
            }
            100% {
                r: 20;
                opacity: 0;
            }
        }

        /* The static dot for the marker (foreground) */
        .marker-dot {
            fill: red;  /* Solid red dot */
        }

        .label {
            fill: black;
            font-size: 20px;
            opacity: 0%;
            transition: all 0.2s;
        }
        
        .label:hover{
            font-size: 30px;
        }
        
        /* Card for city information */
            .info-card {
                position: absolute;
                opacity: 0%;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                transition: all 0.2s;
                text:wrap;
                transform: scale(0.5);
                left: 20px;
                top:100px;
                height:410px;
                max-height:460px;
                display: none;
            }
            
        .color-dist{
            right: 0px;
            top:0px;
        }
        
        #map-wrapper{
            position: relative;
            width: 100%; /* Or a specific width */
            height: calc((9 / 22) * 100vw); /* Height calculated based on width */
        }
        
        #svgMap{
            width: 50%;
            transition: all 0.6s;
            right: 25%;
            top: 40px;
        }

    }

    /* 2. Large Laptop/Desktop Screens (1441px - 2560px) */
    @media (min-width: 1441px) and (max-width: 2560px) {
        
        /* Define the fade-in/fade-out animation */
        @keyframes fadeInOut {
        0% {
            opacity: 0; /* Fully transparent */
            background-position: 0% 50%; /* Start gradient at 0% */
        }
        50% {
            opacity: 1; /* Fully visible */
            background-position: 100% 50%; /* Move gradient to 100% */
        }
        100% {
            opacity: 0; /* Fade out to fully transparent */
            background-position: 0% 50%; /* Back to starting position */
        }
        }

        /* Apply gradient and animation to the text */
        .fade-animation {
        display: inline-block;
        color: orange;
        animation: fadeInOut 4s ease-in-out infinite; /* Duration and infinite loop */
        background-size: 200% auto; /* Ensures smooth gradient transition */
        }

        /* Style for the growing, disappearing circle (background) */
        .marker-animation {
            fill: none;
            stroke: rgba(255, 0, 0, 0.5);  /* Red color with opacity */
            stroke-width: 2;
            animation: grow 2s ease-out infinite;
            transition: all 0.2s;
        }

        /* Keyframe for the growing animation (behind the dot) */
        @keyframes grow {
            0% {
                r: 5;
                opacity: 0.7;
            }
            100% {
                r: 20;
                opacity: 0;
            }
        }

        /* The static dot for the marker (foreground) */
        .marker-dot {
            fill: red;  /* Solid red dot */
        }

        .label {
            fill: black;
            font-size: 20px;
            opacity: 0%;
            transition: all 0.2s;
        }
        
        .label:hover{
            font-size: 30px;
        }
        
        /* Card for city information */
            .info-card {
                position: absolute;
                opacity: 0%;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                transition: all 0.2s;
                text:wrap;
                transform: scale(0.5);
                left: 20px;
                top:100px;
                height:410px;
                max-height:460px;
                display: none;
            }
            
            
            
            
        .color-dist{
            right: 0px;
            top:0px;
            font-size:20px;
        }
        
        .color-wrapper{
            margin-top:17px;
            margin-right:10px;
            width:20px;
            height:15px;
        }
        
        .color-svg{
            width:15px;
            height:15px;
        }
        
        #map-wrapper{
            position: relative;
            width: 100%; /* Or a specific width */
            height: calc((9 / 22) * 100vw); /* Height calculated based on width */
        }
        
        #svgMap{
            width: 50%;
            transition: all 0.6s;
            right: 25%;
            top: 40px;
            margin: auto;
        }
        
        #coordinates{
            font-size:30px;
        }

    }




    /* 3. 4K Ultra HD Screens (2561px and up) */
    @media (min-width: 2561px) {
        /* Define the fade-in/fade-out animation */
        @keyframes fadeInOut {
        0% {
            opacity: 0; /* Fully transparent */
            background-position: 0% 50%; /* Start gradient at 0% */
        }
        50% {
            opacity: 1; /* Fully visible */
            background-position: 100% 50%; /* Move gradient to 100% */
        }
        100% {
            opacity: 0; /* Fade out to fully transparent */
            background-position: 0% 50%; /* Back to starting position */
        }
        }

        /* Apply gradient and animation to the text */
        .fade-animation {
        display: inline-block;
        color: orange;
        animation: fadeInOut 4s ease-in-out infinite; /* Duration and infinite loop */
        background-size: 200% auto; /* Ensures smooth gradient transition */
        }

        /* Style for the growing, disappearing circle (background) */
        .marker-animation {
            fill: none;
            stroke: rgba(255, 0, 0, 0.5);  /* Red color with opacity */
            stroke-width: 2;
            animation: grow 2s ease-out infinite;
            transition: all 0.2s;
        }

        /* Keyframe for the growing animation (behind the dot) */
        @keyframes grow {
            0% {
                r: 5;
                opacity: 0.7;
            }
            100% {
                r: 20;
                opacity: 0;
            }
        }

        /* The static dot for the marker (foreground) */
        .marker-dot {
            fill: red;  /* Solid red dot */
        }

        .label {
            fill: black;
            font-size: 20px;
            opacity: 0%;
            transition: all 0.2s;
        }
        
        .label:hover{
            font-size: 30px;
        }
        
        /* Card for city information */
            .info-card {
                position: absolute;
                opacity: 0%;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                transition: all 0.2s;
                text:wrap;
                transform: scale(0.5);
                left: 20px;
                top:100px;
                height:410px;
                max-height:460px;
                display: none;
            }
            
            
            
        .title{
            font-size: 40px;
        }
            
        .color-dist{
            right: 0px;
            top:0px;
            font-size:35px;
        }
        
        .color-wrapper{
            margin-top:25px;
            margin-right:10px;
            width:20px;
            height:15px;
        }
        
        .color-svg{
            width:30px;
            height:30px;
        }
        
        #map-wrapper{
            position: relative;
            width: 100%; /* Or a specific width */
            height: calc((9 / 22) * 100vw); /* Height calculated based on width */
        }
        
        #svgMap{
            width: 50%;
            transition: all 0.6s;
            right: 25%;
            top: 40px;
        }
        
        #coordinates{
            font-size:30px;
        }

    }
    
    
    
    
    @media (min-width: 3830px) {
        /* Define the fade-in/fade-out animation */
        @keyframes fadeInOut {
        0% {
            opacity: 0; /* Fully transparent */
            background-position: 0% 50%; /* Start gradient at 0% */
        }
        50% {
            opacity: 1; /* Fully visible */
            background-position: 100% 50%; /* Move gradient to 100% */
        }
        100% {
            opacity: 0; /* Fade out to fully transparent */
            background-position: 0% 50%; /* Back to starting position */
        }
        }

        /* Apply gradient and animation to the text */
        .fade-animation {
        display: inline-block;
        color: orange;
        animation: fadeInOut 4s ease-in-out infinite; /* Duration and infinite loop */
        background-size: 200% auto; /* Ensures smooth gradient transition */
        }

        /* Style for the growing, disappearing circle (background) */
        .marker-animation {
            fill: none;
            stroke: rgba(255, 0, 0, 0.5);  /* Red color with opacity */
            stroke-width: 2;
            animation: grow 2s ease-out infinite;
            transition: all 0.2s;
        }

        /* Keyframe for the growing animation (behind the dot) */
        @keyframes grow {
            0% {
                r: 5;
                opacity: 0.7;
            }
            100% {
                r: 20;
                opacity: 0;
            }
        }

        /* The static dot for the marker (foreground) */
        .marker-dot {
            fill: red;  /* Solid red dot */
        }

        .label {
            fill: black;
            font-size: 20px;
            opacity: 0%;
            transition: all 0.2s;
        }
        
        .label:hover{
            font-size: 30px;
        }
        
        /* Card for city information */
            .info-card {
                position: absolute;
                opacity: 0%;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                transition: all 0.2s;
                text:wrap;
                transform: scale(0.5);
                left: 20px;
                top:100px;
                height:410px;
                max-height:460px;
                display: none;
            }
            
            
            
        #title{
            font-size: 40px;
        }
            
        .color-dist{
            right: 0px;
            top:0px;
            font-size:35px;
        }
        
        .color-wrapper{
            margin-top:20px;
            margin-right:14px;
            width:20px;
            height:15px;
        }
        
        .color-svg{
            width:30px;
            height:30px;
        }
        
        #map-wrapper{
            position: relative;
            height: 90vh;
        }
        
        #svgMap{
            width: 50%;
            transition: all 0.6s;
            right: 25%;
            top: 40px;
        }
        
        #coordinates{
            font-size:35px;
        }

    }
</style>
"""

scripting = """

<script>

// Select all regions from the map by their class or ID
const regions = document.querySelectorAll('.group');  // '.group' is the class assigned to map elements


function clickHandler(id){
    let cluster = document.getElementById("cluster-info");
    document.getElementById("cluster-info").classList.add('hidden');
}

document.addEventListener("DOMContentLoaded", function () {
    // Select the SVG element
    const svgMap = document.querySelector("svg");

    // Define locations for makkah and Riyadh
    const locations = [
        {
            name: "Makkah",
            x: 220, // Approximate X-coordinate for Makkah
            y: 440, // Approximate Y-coordinate for Makkah
        },
        {
            name: "Riyadh",
            x: 500, // Approximate X-coordinate for Riyadh
            y: 300, // Approximate Y-coordinate for Riyadh
        },
        {
            name: "Qunfudah",
            x: 270, // Approximate X-coordinate for Qunfudah
            y: 520, // Approximate Y-coordinate for Qunfudah
        },
        {
            name: "Kamel",
            x: 220, // Approximate X-coordinate for Kamel
            y: 384, // Approximate Y-coordinate for Kamel
        },
        {
            name: "Khulis",
            x: 200, // Approximate X-coordinate for Khulis
            y: 400, // Approximate Y-coordinate for Khulis
        },
        {
            name: "Madinah",
            x: 200, // Approximate X-coordinate for Madinah
            y: 312, // Approximate Y-coordinate for Madinah
        },
        
    ];

    // Function to add marker with animation behind the dot
    function addMarker(location, delay, backgroundColor = "rgba(0, 0, 0, 0.2)") {
        setTimeout(() => {
            // Create the background area for the city
            const backgroundArea = document.createElementNS("http://www.w3.org/2000/svg", "rect");
            backgroundArea.setAttribute("x", location.x - 15); // Adjust positioning as needed
            backgroundArea.setAttribute("y", location.y - 15); // Adjust positioning as needed
            backgroundArea.setAttribute("width", 30); // Set width of the background area
            backgroundArea.setAttribute("height", 30); // Set height of the background area
            backgroundArea.setAttribute("fill", backgroundColor); // Set the background color
            backgroundArea.setAttribute("rx", 10); // Rounded corners (optional)
            backgroundArea.setAttribute("ry", 10); // Rounded corners (optional)
            backgroundArea.style.display = "none";

            // Create the growing circle (background animation)
            const animatedCircle = document.createElementNS("http://www.w3.org/2000/svg", "circle");
            animatedCircle.setAttribute("cx", location.x);
            animatedCircle.setAttribute("cy", location.y);
            animatedCircle.setAttribute("r", 5);
            animatedCircle.classList.add("marker-animation");

            // Create the static dot (foreground)
            const staticDot = document.createElementNS("http://www.w3.org/2000/svg", "circle");
            staticDot.setAttribute("cx", location.x);
            staticDot.setAttribute("cy", location.y);
            staticDot.setAttribute("r", 5);
            staticDot.classList.add("marker-dot");

            // Create a label for the location
            const label = document.createElementNS("http://www.w3.org/2000/svg", "text");
            label.setAttribute("x", location.x + 10); // Offset label positioning
            label.setAttribute("y", location.y - 10);
            label.setAttribute("id", String(location.name).toLowerCase());
            label.classList.add("label");
            label.classList.add("font-bold", "cursor-pointer");
            label.textContent = location.name;

            // Append the background area, animated circle, static dot, and label to the SVG
            svgMap.appendChild(backgroundArea); // Background area
            svgMap.appendChild(animatedCircle);  // Background animation
            svgMap.appendChild(staticDot);       // Foreground static dot
            svgMap.appendChild(label);           // Label

            // Make the label visible after the marker appears
            setTimeout(() => {
                label.style.opacity = "100%";
            }, 1000);  // Label appears after 1 second
        }, delay);  // Apply delay before adding the marker
    }


    // Add markers one at a time with delays (Mecca first, then Riyadh)
    addMarker(locations[0], 250, "#b91c1c");  // Add Mecca after 0.5 second
    addMarker(locations[1], 1000, "#fde047");  // Add Riyadh after 2 seconds
    addMarker(locations[2], 1500, "#dcfce7");  // Add Qunfudah after 2 seconds
    addMarker(locations[3], 1750, "#15803d");  // Add Khulis after 2 seconds
    addMarker(locations[4], 2000, "#86efac");  // Add Kamel after 2 seconds
    addMarker(locations[5], 2100, "#86efac");  // Add Kamel after 2 seconds
    
});

function measureWindowWidth() {
    const windowWidth = window.innerWidth; // Get the current width of the window
    console.log(`Window width: ${windowWidth}px`);
    
}

// Add event listener to the window resize event
window.addEventListener('resize', measureWindowWidth);

// Call the function initially to log the width when the page is first loaded
measureWindowWidth();

function toggleCard(city, state) {
    const cards = ['makkah', 'riyadh', 'qunfudah', 'kamel', 'khulis', 'madinah'];
    const cardElements = cards.map(city => document.getElementById(`${city}-card`));
    const svgMap = document.getElementById("svgMap");

    const currentCard = document.getElementById(`${city}-card`);

    cardElements.forEach(card => {
        // Only apply display: none after a delay if the card is currently shown
        if (card.dataset.toggle === 'on') {
            card.style.opacity = '0';
            card.style.transform = 'scale(0.5)';

            // Set display: none after the transition ends (e.g., 300ms)
            setTimeout(() => {
                card.style.display = 'none';
            }, 300); // Adjust this to match the transition duration in CSS
        }
        if (card != currentCard){
            card.dataset.toggle = 'off';
        }
            
    });
    
    if (state === 'blur') {
        currentCard.dataset.toggle = 'off';
        currentCard.style.opacity = '0';
        currentCard.style.transform = 'scale(0.5)';

        // Hide the card after the transition completes
        setTimeout(() => {
            currentCard.style.display = 'none';
        }, 300); // Match this with CSS transition duration
        currentCard.dataset.toggle = 'off';
        
        if (window.innerWidth >= 3000){
            
            if (city == 'riyadh'){
                svgMap.style.right = "25%";
                svgMap.style.top = "100px";
                svgMap.style.transform = "scale(1)"
            }
            else{
                svgMap.style.right = "25%";
                svgMap.style.top = "100px";
                svgMap.style.transform = "scale(1)"
            }    
                    
        } else {
            
            if (city == 'riyadh'){
                svgMap.style.right = "25%";
                svgMap.style.top = "40px";
                svgMap.style.transform = "scale(1)"
            }
            else {
                svgMap.style.right = "25%";
                svgMap.style.top = "40px";
                svgMap.style.transform = "scale(1)"
            }
            
        }
        
    } else if (currentCard.dataset.toggle === 'off') {
        currentCard.style.display = 'block';  // Make it block before animations
        // Trigger animations
        setTimeout(() => {
            currentCard.style.opacity = '1';
            
            if (window.innerWidth < 1700){
                currentCard.style.transform = 'scale(1)';
            }
            
            else if (window.innerWidth >= 1700 && window.innerWidth < 2000){
                currentCard.style.marginLeft = '60px';
                currentCard.style.marginTop = '60px';
                currentCard.style.transform = 'scale(1.1)';
            }
            else if (window.innerWidth >= 2000 && window.innerWidth < 2560){
                currentCard.style.marginLeft = '100px';
                currentCard.style.marginTop = '100px';
                currentCard.style.transform = 'scale(1.3)';
            }
            
            else if (window.innerWidth >= 2561 && window.innerWidth < 3600){
                currentCard.style.marginLeft = '200px';
                currentCard.style.marginTop = '200px';
                currentCard.style.transform = 'scale(1.7)';
            }
            else if (window.innerWidth >= 3600){
                currentCard.style.marginLeft = '500px';
                currentCard.style.marginTop = '500px';
                currentCard.style.transform = 'scale(2.7)';
            }
            // currentCard.style.transform = 'scale(1)';
        }, 10); // Slight delay to ensure CSS transition takes effect

        currentCard.dataset.toggle = 'on';
        
        if (window.innerWidth < 1440){
            
            if (city == 'riyadh'){
                svgMap.style.right = "250px";
                svgMap.style.top = "100px";
                svgMap.style.transform = "scale(1.7)"
            }
            else if (city == 'madinah'){
                svgMap.style.right = "180px";
                svgMap.style.top = "60px";
                svgMap.style.transform = "scale(1.7)"
            }
            else if (city == 'qunfudah'){
                svgMap.style.right = "180px";
                svgMap.style.top = "-80px";
                svgMap.style.transform = "scale(1.7)"
            }
            else{
                svgMap.style.right = "180px";
                svgMap.style.top = "0px";
                svgMap.style.transform = "scale(1.7)"
            }
            
        }
        
        else if (window.innerWidth >= 1440 && window.innerWidth < 2560){
            
            if (city == 'riyadh'){
                svgMap.style.right = "250px";
                svgMap.style.top = "100px";
                svgMap.style.transform = "scale(1.7)"
            }
            else if (city == 'madinah'){
                svgMap.style.right = "180px";
                svgMap.style.top = "60px";
                svgMap.style.transform = "scale(1.7)"
            }
            else if (city == 'qunfudah'){
                svgMap.style.right = "180px";
                svgMap.style.top = "-80px";
                svgMap.style.transform = "scale(1.7)"
            }
            else{
                svgMap.style.right = "180px";
                svgMap.style.top = "0px";
                svgMap.style.transform = "scale(1.7)"
            }
            
        }
        
        else if (window.innerWidth >= 2560 && window.innerWidth < 3000){
            
            if (city == 'riyadh'){
                svgMap.style.right = "600px";
                svgMap.style.top = "100px";
                svgMap.style.transform = "scale(1.7)"
            }
            else if (city == 'madinah'){
                svgMap.style.right = "180px";
                svgMap.style.top = "60px";
                svgMap.style.transform = "scale(1.7)"
            }
            else if (city == 'qunfudah'){
                svgMap.style.right = "180px";
                svgMap.style.top = "-140px";
                svgMap.style.transform = "scale(1.7)"
            }
            else{
                svgMap.style.right = "300px";
                svgMap.style.top = "0px";
                svgMap.style.transform = "scale(1.7)"
            }
            
        }
        
        else if (window.innerWidth >= 3000){
            
            if (city == 'riyadh'){
                svgMap.style.right = "750px";
                svgMap.style.top = "100px";
                svgMap.style.transform = "scale(1.7)"
            }
            else if (city == 'madinah'){
                svgMap.style.right = "550px";
                svgMap.style.top = "60px";
                svgMap.style.transform = "scale(1.7)"
            }
            else if (city == 'qunfudah'){
                svgMap.style.right = "550px";
                svgMap.style.top = "-80px";
                svgMap.style.transform = "scale(1.7)"
            }
            else{
                svgMap.style.right = "550px";
                svgMap.style.top = "0px";
                svgMap.style.transform = "scale(1.7)"
            }
            
        }
        
    } else {
        currentCard.style.opacity = '0';
        currentCard.style.transform = 'scale(0.5)';

        // Hide the card after the transition completes
        setTimeout(() => {
            currentCard.style.display = 'none';
        }, 300); // Match this with CSS transition duration
        currentCard.dataset.toggle = 'off';
        
        if (window.innerWidth >= 3000){
            
            if (city == 'riyadh'){
                svgMap.style.right = "25%";
                svgMap.style.top = "100px";
                svgMap.style.transform = "scale(1)"
            }
            else{
                svgMap.style.right = "25%";
                svgMap.style.top = "100px";
                svgMap.style.transform = "scale(1)"
            }    
                    
        } else {
            
            if (city == 'riyadh'){
                svgMap.style.right = "25%";
                svgMap.style.top = "40px";
                svgMap.style.transform = "scale(1)"
            }
            else {
                svgMap.style.right = "25%";
                svgMap.style.top = "40px";
                svgMap.style.transform = "scale(1)"
            }
            
        }
    }
    
}


function setMapStyle(width, right, height, top) {
    const svgMap = document.getElementById("svgMap");
    svgMap.style.width = width;
    svgMap.style.right = right;
    document.getElementById("map-wrapper").style.height = height;
    svgMap.style.top = top;
}



function openFacility(id){
    console.log(id)
    let facility = document.getElementById(id)
    
    if (facility.dataset.open == 'false'){
        facility.style.height = '280px';
        facility.dataset.open = 'true'
        document.querySelector(`#${id} #info`).style.height = '0px'
    }
    else{
        facility.style.height = '0px';
        facility.dataset.open = 'false'
        document.querySelector(`#${id} #info`).style.height = 'auto'
    }
    
}

setTimeout(() => {console.log('wait for it')}, 2000)

let makkahLabel = 'document.querySelector("#makkah")'
let riyadhLabel = 'document.querySelector("#riyadh")'
let kamelLabel = 'document.querySelector("#kamel")'
let khulisLabel = 'document.querySelector("#khulis")'
let qunfudahLabel = 'document.querySelector("#qunfudah")'
let madinahLabel = 'document.querySelector("#madinah")'

setTimeout(() => {
let makkahLabel = document.querySelector("#makkah")
let riyadhLabel = document.querySelector("#riyadh")
let kamelLabel = document.querySelector("#kamel")
let khulisLabel = document.querySelector("#khulis")
let qunfudahLabel = document.querySelector("#qunfudah")
let madinahLabel = document.querySelector("#madinah")



makkahLabel.addEventListener("click", function() {
    toggleCard('makkah', 'click');
});

riyadhLabel.addEventListener("click", function() {
    toggleCard('riyadh', 'click');
});

kamelLabel.addEventListener("click", function() {
    toggleCard('kamel', 'click');
});

khulisLabel.addEventListener('click', function() {
    toggleCard('khulis', 'click');
});

qunfudahLabel.addEventListener("click", function() {
    toggleCard('qunfudah', 'click');
});


madinahLabel.addEventListener("click", function() {
    toggleCard('madinah', 'click');
});



riyadhLabel.style.outline = "none"

makkahLabel.style.outline = "none"

kamelLabel.style.outline = "none"

khulisLabel.style.outline = "none"

qunfudahLabel.style.outline = "none"

madinahLabel.style.outline = "none"

}, 2500)

// Get the SVG element
const svgMap = document.getElementById('svgMap');
const coordinatesDisplay = document.getElementById('coordinates');

// Function to get the mouse position relative to the SVG
function getMousePosition(event) {
    const svgPoint = svgMap.createSVGPoint();
    svgPoint.x = event.clientX;
    svgPoint.y = event.clientY;

    // Get the transformation matrix of the SVG
    const ctm = svgMap.getScreenCTM().inverse();

    // Convert mouse position to SVG coordinates
    const transformedPoint = svgPoint.matrixTransform(ctm);

    return {
        x: transformedPoint.x,
        y: transformedPoint.y
    };
}

// Add event listener for mouse movement
svgMap.addEventListener('mousemove', (event) => {
    const coords = getMousePosition(event);
    coordinatesDisplay.textContent = `X: ${coords.x.toFixed(2)}, Y: ${coords.y.toFixed(2)}`;
});



// Function to measure the width of the window
function measureWindowWidth() {
    const windowWidth = window.innerWidth; // Get the current width of the window
    console.log(`Window width: ${windowWidth}px`);
}

// Add event listener to the window resize event
window.addEventListener('resize', measureWindowWidth);

// Call the function initially to log the width when the page is first loaded
measureWindowWidth();
</script>
"""


makkah = f"""

<div class="info-card overflow-hidden makkah-card text-center bg-gradient-to-tr from-black to-gray-900 border border-red-500 w-auto text-white rounded-xl p-5" data-toggle="off" id="makkah-card">
    
    <div class="w-full bg-transparent border-0 justify-end text-center flex items-center">
        <button class="w-auto bg-transparent border-0 outline-none text-center"
        onmousedown="toggleCard('makkah', 'blur');">
            <i class="fa-solid fa-xmark text-red-500 text-2xl pb-1"></i>
        </button>
    </div>
    
    <button class="w-full overflow-hidden group bg-transparent border-0 justify-center outline-none text-center flex gap-3 items-center"
     onmousedown="openFacility('makkah-facility')"
     id="makkah-button">
        <h1 class="text-4xl font-bold mb-4">Makkah City</h1>
        <i class="fa-solid fa-angle-down text-2xl pb-1"></i>
    </button>
    
    <div class="h-0 mb-2 transition-all overflow-auto" id="makkah-facility" style="transition: all 0.3s;" data-open="false">
    
        <div class="group rounded-2xl p-2 mb-3 text-wrap" id="makkah-facility-3"
         onmouseover="document.getElementById('makkah-facility-info-3').style.height = '80px'"
         onmouseout="document.getElementById('makkah-facility-info-3').style.height = '0px'"
         style="background-color: #090F1EFF">
         
            <h3 class="text-2xl font-bold my-3">{facility_data.iloc[3]['FACILITY_NAME_EN']}</h3>
            
            <div class="h-0 flex overflow-hidden mb-2 justify-center" id="makkah-facility-info-3" style="display:flex;transition: all 0.3s;">
                <div class="text-center p-3 rounded-2xl">
                    <h1 class="text-xl font-bold mb-1">{facility_data.iloc[3]['Total_Occupied']}</h1>
                    <p class="text-md text-gray-400">Total Occupied</p>
                </div>
                <div class="text-center mx-2 bg-gray-900 p-3 rounded-lg">
                    <h1 class="text-xl font-bold mb-1 text-red-500">{round((facility_data.iloc[3]['Occupancy_Rate'] * 100), 2)}%</h1>
                    <p class="text-md text-gray-400">Occupancy Rate</p>
                </div>
                <div class="text-center p-3 rounded-lg">
                    <h1 class="text-xl font-bold mb-1">{facility_data.iloc[3]['Total_Vacant']}</h1>
                    <p class="text-md text-gray-400">Total Vacant</p>
                </div>
            </div>
        </div>
    
        <div class="group rounded-2xl p-2 mb-3 text-wrap" id="makkah-facility-4"
         onmouseover="document.getElementById('makkah-facility-info-4').style.height = '80px'"
         onmouseout="document.getElementById('makkah-facility-info-4').style.height = '0px'"
         style="background-color: #090F1EFF">
         
            <h3 class="text-2xl font-bold my-3">{facility_data.iloc[4]['FACILITY_NAME_EN']}</h3>
            
            <div class="h-0 flex overflow-hidden mb-2 justify-center" id="makkah-facility-info-4" style="display:flex;transition: all 0.3s;">
                <div class="text-center p-3 rounded-2xl">
                    <h1 class="text-xl font-bold mb-1">{facility_data.iloc[4]['Total_Occupied']}</h1>
                    <p class="text-md text-gray-400">Total Occupied</p>
                </div>
                <div class="text-center mx-2 bg-gray-900 p-3 rounded-lg">
                    <h1 class="text-xl font-bold mb-1 text-yellow-500">{round((facility_data.iloc[4]['Occupancy_Rate'] * 100), 2)}%</h1>
                    <p class="text-md text-gray-400">Occupancy Rate</p>
                </div>
                <div class="text-center p-3 rounded-lg">
                    <h1 class="text-xl font-bold mb-1">{facility_data.iloc[4]['Total_Vacant']}</h1>
                    <p class="text-md text-gray-400">Total Vacant</p>
                </div>
            </div>
        </div>
    
        <div class="group rounded-2xl p-2 mb-3 text-wrap" id="makkah-facility-5"
         onmouseover="document.getElementById('makkah-facility-info-5').style.height = '80px'"
         onmouseout="document.getElementById('makkah-facility-info-5').style.height = '0px'"
         style="background-color: #090F1EFF">
         
            <h3 class="text-2xl font-bold my-3">{facility_data.iloc[5]['FACILITY_NAME_EN']}</h3>
            
            <div class="h-0 flex overflow-hidden mb-2 justify-center" id="makkah-facility-info-5" style="display:flex;transition: all 0.3s;">
                <div class="text-center p-3 rounded-2xl">
                    <h1 class="text-xl font-bold mb-1">{facility_data.iloc[5]['Total_Occupied']}</h1>
                    <p class="text-md text-gray-400">Total Occupied</p>
                </div>
                <div class="text-center mx-2 bg-gray-900 p-3 rounded-lg">
                    <h1 class="text-xl font-bold mb-1 text-green-300">{round((facility_data.iloc[5]['Occupancy_Rate'] * 100), 2)}%</h1>
                    <p class="text-md text-gray-400">Occupancy Rate</p>
                </div>
                <div class="text-center p-3 rounded-lg">
                    <h1 class="text-xl font-bold mb-1">{facility_data.iloc[5]['Total_Vacant']}</h1>
                    <p class="text-md text-gray-400">Total Vacant</p>
                </div>
            </div>
        </div>
    
        <div class="group rounded-2xl p-2 mb-3 text-wrap" id="makkah-facility-6"
         onmouseover="document.getElementById('makkah-facility-info-6').style.height = '80px'"
         onmouseout="document.getElementById('makkah-facility-info-6').style.height = '0px'"
         style="background-color: #090F1EFF">
         
            <h3 class="text-2xl font-bold my-3">{facility_data.iloc[6]['FACILITY_NAME_EN']}</h3>
            
            <div class="h-0 flex overflow-hidden mb-2 justify-center" id="makkah-facility-info-6" style="display:flex;transition: all 0.3s;">
                <div class="text-center p-3 rounded-2xl">
                    <h1 class="text-xl font-bold mb-1">{facility_data.iloc[6]['Total_Occupied']}</h1>
                    <p class="text-md text-gray-400">Total Occupied</p>
                </div>
                <div class="text-center mx-2 bg-gray-900 p-3 rounded-lg">
                    <h1 class="text-xl font-bold mb-1 text-red-700">{round((facility_data.iloc[6]['Occupancy_Rate'] * 100), 2)}%</h1>
                    <p class="text-md text-gray-400">Occupancy Rate</p>
                </div>
                <div class="text-center p-3 rounded-lg">
                    <h1 class="text-xl font-bold mb-1">{facility_data.iloc[6]['Total_Vacant']}</h1>
                    <p class="text-md text-gray-400">Total Vacant</p>
                </div>
            </div>
        </div>
        
    
        <div class="group rounded-2xl p-2 mb-3 text-wrap" id="makkah-facility-7"
         onmouseover="document.getElementById('makkah-facility-info-7').style.height = '80px'"
         onmouseout="document.getElementById('makkah-facility-info-7').style.height = '0px'"
         style="background-color: #090F1EFF">
         
            <h3 class="text-2xl font-bold my-3">{facility_data.iloc[7]['FACILITY_NAME_EN']}</h3>
            
            <div class="h-0 flex overflow-hidden mb-2 justify-center" id="makkah-facility-info-7" style="display:flex;transition: all 0.3s;">
                <div class="text-center p-3 rounded-2xl">
                    <h1 class="text-xl font-bold mb-1">{facility_data.iloc[7]['Total_Occupied']}</h1>
                    <p class="text-md text-gray-400">Total Occupied</p>
                </div>
                <div class="text-center mx-2 bg-gray-900 p-3 rounded-lg">
                    <h1 class="text-xl font-bold mb-1 text-red-500">{round((facility_data.iloc[7]['Occupancy_Rate'] * 100), 2)}%</h1>
                    <p class="text-md text-gray-400">Occupancy Rate</p>
                </div>
                <div class="text-center p-3 rounded-lg">
                    <h1 class="text-xl font-bold mb-1">{facility_data.iloc[7]['Total_Vacant']}</h1>
                    <p class="text-md text-gray-400">Total Vacant</p>
                </div>
            </div>
        </div>
        
    
        <div class="group rounded-2xl p-2 mb-3 text-wrap" id="makkah-facility-8"
         onmouseover="document.getElementById('makkah-facility-info-8').style.height = '80px'"
         onmouseout="document.getElementById('makkah-facility-info-8').style.height = '0px'"
         style="background-color: #090F1EFF">
         
            <h3 class="text-2xl font-bold my-3">{facility_data.iloc[8]['FACILITY_NAME_EN']}</h3>
            
            <div class="h-0 flex overflow-hidden mb-2 justify-center" id="makkah-facility-info-8" style="display:flex;transition: all 0.3s;">
                <div class="text-center p-3 rounded-2xl">
                    <h1 class="text-xl font-bold mb-1">{facility_data.iloc[8]['Total_Occupied']}</h1>
                    <p class="text-md text-gray-400">Total Occupied</p>
                </div>
                <div class="text-center mx-2 bg-gray-900 p-3 rounded-lg">
                    <h1 class="text-xl font-bold mb-1 text-red-500">{round((facility_data.iloc[8]['Occupancy_Rate'] * 100), 2)}%</h1>
                    <p class="text-md text-gray-400">Occupancy Rate</p>
                </div>
                <div class="text-center p-3 rounded-lg">
                    <h1 class="text-xl font-bold mb-1">{facility_data.iloc[8]['Total_Vacant']}</h1>
                    <p class="text-md text-gray-400">Total Vacant</p>
                </div>
            </div>
        </div>
        
    
        <div class="group rounded-2xl p-2 mb-3 text-wrap" id="makkah-facility-9"
         onmouseover="document.getElementById('makkah-facility-info-9').style.height = '80px'"
         onmouseout="document.getElementById('makkah-facility-info-9').style.height = '0px'"
         style="background-color: #090F1EFF">
         
            <h3 class="text-2xl font-bold my-3">{facility_data.iloc[9]['FACILITY_NAME_EN']}</h3>
            
            <div class="h-0 flex overflow-hidden mb-2 justify-center" id="makkah-facility-info-9" style="display:flex;transition: all 0.3s;">
                <div class="text-center p-3 rounded-2xl">
                    <h1 class="text-xl font-bold mb-1">{facility_data.iloc[9]['Total_Occupied']}</h1>
                    <p class="text-md text-gray-400">Total Occupied</p>
                </div>
                <div class="text-center mx-2 bg-gray-900 p-3 rounded-lg">
                    <h1 class="text-xl font-bold mb-1 text-red-500">{round((facility_data.iloc[9]['Occupancy_Rate'] * 100), 2)}%</h1>
                    <p class="text-md text-gray-400">Occupancy Rate</p>
                </div>
                <div class="text-center p-3 rounded-lg">
                    <h1 class="text-xl font-bold mb-1">{facility_data.iloc[9]['Total_Vacant']}</h1>
                    <p class="text-md text-gray-400">Total Vacant</p>
                </div>
            </div>
        </div>
        
    </div>
    <div class="mb-2 justify-between">
        <div class="text-center p-3 rounded-2xl">
            <h1 class="text-4xl font-bold mb-1">{cluster_data.iloc[3]['Total_Occupied']}</h1>
            <p class="text-md text-gray-400">Total Occupied</p>
        </div>
        <div class="text-center p-3 rounded-2xl">
            <h1 class="text-4xl font-bold mb-1">{cluster_data.iloc[3]['Total_Vacant']}</h1>
            <p class="text-md text-gray-400">Total Vacant</p>
        </div>
        <div class="w-100 text-center mx-2 bg-gray-900 p-3 rounded-2xl">
            <h1 class="text-4xl font-bold mb-1 text-red-500">{round((cluster_data.iloc[3]['Occupancy_Rate'] * 100), 2)}%</h1>
            <p class="text-md text-gray-400">Occupancy Rate</p>
        </div>
    </div>
</div>



"""

riyadh = f"""

<div class="info-card overflow-hidden riyadh-card text-center bg-gradient-to-tr from-black to-gray-900 border border-yellow-500 text-white w-auto text-auto rounded-xl p-5" data-toggle="off" id="riyadh-card">

    <div class="w-full bg-transparent border-0 justify-end text-center flex items-center">
        <button class="w-auto bg-transparent border-0 outline-none text-center"
        onmousedown="toggleCard('riyadh', 'blur');">
            <i class="fa-solid fa-xmark text-yellow-500 text-2xl pb-1"></i>
        </button>
    </div>
    
    <button class="w-full overflow-hidden group bg-transparent border-0 justify-center outline-none text-center flex gap-3 items-center"
     onmousedown="openFacility('riyadh-facility')"
     id="riyadh-button">
        <h1 class="text-4xl font-bold mb-4">Riyadh City</h1>
        <i class="fa-solid fa-angle-down text-2xl pb-1"></i>
    </button>
    
    <div class="h-0 mb-2 transition-all overflow-auto" id="riyadh-facility" style="transition: all 0.3s;" data-open="false">
    
        <div class="group rounded-2xl p-2 mb-3 text-wrap" id="riyadh-facility-1"
         onmouseover="document.getElementById('riyadh-facility-info-1').style.height = '80px'"
         onmouseout="document.getElementById('riyadh-facility-info-1').style.height = '0px'"
         style="background-color: #090F1EFF">
         
            <h3 class="text-2xl font-bold my-3">{facility_data.iloc[13]['FACILITY_NAME_EN']}</h3>
            
            <div class="h-0 flex overflow-hidden mb-2 justify-center" id="riyadh-facility-info-1" style="display:flex;transition: all 0.3s;">
                <div class="text-center p-3 rounded-2xl">
                    <h1 class="text-xl font-bold mb-1">{facility_data.iloc[13]['Total_Occupied']}</h1>
                    <p class="text-md text-gray-400">Total Occupied</p>
                </div>
                <div class="text-center mx-2 bg-gray-900 p-3 rounded-lg">
                    <h1 class="text-xl font-bold mb-1 text-yellow-500">{round((facility_data.iloc[13]['Occupancy_Rate'] * 100), 2)}%</h1>
                    <p class="text-md text-gray-400">Occupancy Rate</p>
                </div>
                <div class="text-center p-3 rounded-lg">
                    <h1 class="text-xl font-bold mb-1">{facility_data.iloc[13]['Total_Vacant']}</h1>
                    <p class="text-md text-gray-400">Total Vacant</p>
                </div>
            </div>
        </div>
        
        <div class="group rounded-2xl p-2 mb-3 text-wrap" id="riyadh-facility-2"
         onmouseover="document.getElementById('riyadh-facility-info-2').style.height = '80px'"
         onmouseout="document.getElementById('riyadh-facility-info-2').style.height = '0px'"
         style="background-color: #090F1EFF">
         
            <h3 class="text-2xl font-bold my-3">{facility_data.iloc[14]['FACILITY_NAME_EN']}</h3>
            
            <div class="h-0 flex overflow-hidden mb-2 justify-center" id="riyadh-facility-info-2" style="display:flex;transition: all 0.3s;">
                <div class="text-center p-3 rounded-2xl">
                    <h1 class="text-xl font-bold mb-1">{facility_data.iloc[14]['Total_Occupied']}</h1>
                    <p class="text-md text-gray-400">Total Occupied</p>
                </div>
                <div class="text-center mx-2 bg-gray-900 p-3 rounded-lg">
                    <h1 class="text-xl font-bold mb-1 text-green-600">{round((facility_data.iloc[14]['Occupancy_Rate'] * 100), 2)}%</h1>
                    <p class="text-md text-gray-400">Occupancy Rate</p>
                </div>
                <div class="text-center p-3 rounded-lg">
                    <h1 class="text-xl font-bold mb-1">{facility_data.iloc[14]['Total_Vacant']}</h1>
                    <p class="text-md text-gray-400">Total Vacant</p>
                </div>
            </div>
        </div>
        
    </div>
    
    <div class="mb-2 justify-between">
        <div class="text-center p-3 rounded-2xl">
            <h1 class="text-4xl font-bold mb-1">{cluster_data.iloc[5]['Total_Occupied']}</h1>
            <p class="text-md text-gray-400">Total Occupied</p>
        </div>
        <div class="text-center p-3 rounded-2xl">
            <h1 class="text-4xl font-bold mb-1">{cluster_data.iloc[5]['Total_Vacant']}</h1>
            <p class="text-md text-gray-400">Total Vacant</p>
        </div>
        <div class="w-100 text-center mx-auto bg-gray-900 p-3 rounded-2xl">
            <h1 class="text-4xl font-bold mb-1 text-yellow-500">{round((cluster_data.iloc[5]['Occupancy_Rate'] * 100), 2)}%</h1>
            <p class="text-md text-gray-400">Occupancy Rate</p>
        </div>
    </div>
    
</div>


"""

kamel = f"""

<div class="info-card overflow-hidden kamel-card text-center bg-gradient-to-tr from-black to-gray-900 end-0 border border-green-300 text-white w-auto text-auto rounded-xl p-5" data-toggle="off" id="kamel-card">
    
    <div class="w-full bg-transparent border-0 justify-end text-center flex items-center">
        <button class="w-auto bg-transparent border-0 outline-none text-center"
        onmousedown="toggleCard('kamel', 'blur');">
            <i class="fa-solid fa-xmark text-green-300 text-2xl pb-1"></i>
        </button>
    </div>
    
    <button class="w-full overflow-hidden group bg-transparent border-0 justify-center outline-none text-center flex gap-3 items-center"
     onmousedown="openFacility('kamel-facility')"
     id="kamel-button">
        <h1 class="text-4xl font-bold mb-4">Kamel City</h1>
        <i class="fa-solid fa-angle-down text-2xl pb-1"></i>
    </button>
    
    <div class="h-0 mb-2 transition-all overflow-auto" id="kamel-facility" style="transition: all 0.3s;" data-open="false">
    
        <div class="group rounded-2xl p-2 mb-3 text-wrap" id="kamel-facility-1"
         onmouseover="document.getElementById('kamel-facility-info-1').style.height = '80px'"
         onmouseout="document.getElementById('kamel-facility-info-1').style.height = '0px'"
         style="background-color: #090F1EFF">
         
            <h3 class=" text-2xl font-bold my-3">{facility_data.iloc[0]['FACILITY_NAME_EN']}</h3>
            
            <div class="h-0 flex overflow-hidden mb-2 justify-center" id="kamel-facility-info-1" style="display:flex;transition: all 0.3s;">
                <div class="text-center p-3 rounded-2xl">
                    <h1 class="text-xl font-bold mb-1">{facility_data.iloc[0]['Total_Occupied']}</h1>
                    <p class="text-md text-gray-400">Total Occupied</p>
                </div>
                <div class="text-center mx-2 bg-gray-900 p-3 rounded-lg">
                    <h1 class="text-xl font-bold mb-1 text-green-300">{round((facility_data.iloc[0]['Occupancy_Rate'] * 100), 2)}%</h1>
                    <p class="text-md text-gray-400">Occupancy Rate</p>
                </div>
                <div class="text-center p-3 rounded-lg">
                    <h1 class="text-xl font-bold mb-1">{facility_data.iloc[0]['Total_Vacant']}</h1>
                    <p class="text-md text-gray-400">Total Vacant</p>
                </div>
            </div>
        </div>
        
    </div>
    
    <div class="mb-2 justify-between">
        <div class="text-center p-3 rounded-2xl">
            <h1 class="text-4xl font-bold mb-1">{cluster_data.iloc[0]['Total_Occupied']}</h1>
            <p class="text-md text-gray-400">Total Occupied</p>
        </div>
        <div class="text-center p-3 rounded-2xl">
            <h1 class="text-4xl font-bold mb-1">{cluster_data.iloc[0]['Total_Vacant']}</h1>
            <p class="text-md text-gray-400">Total Vacant</p>
        </div>
        <div class="w-100 text-center mx-2 bg-gray-900 p-3 rounded-2xl">
            <h1 class="text-4xl font-bold mb-1 text-green-300">{round((cluster_data.iloc[0]['Occupancy_Rate'] * 100), 2)}%</h1>
            <p class="text-md text-gray-400">Occupancy Rate</p>
        </div>
    </div>
    
</div>


"""

khulis = f"""

<div class="info-card overflow-hidden khulis-card text-center bg-gradient-to-tr from-black to-gray-900 end-0 border border-green-600 text-white w-auto text-auto rounded-xl p-5" data-toggle="off" id="khulis-card">
    
    <div class="w-full bg-transparent border-0 justify-end text-center flex items-center">
        <button class="w-auto bg-transparent border-0 outline-none text-center"
        onmousedown="toggleCard('khulis', 'blur');">
            <i class="fa-solid fa-xmark text-green-600 text-2xl pb-1"></i>
        </button>
    </div>
    
    <button class="w-full overflow-hidden group bg-transparent border-0 justify-center outline-none text-center flex gap-3 items-center"
     onmousedown="openFacility('khulis-facility')"
     id="khulis-button">
        <h1 class="text-4xl font-bold mb-4">Khulis City</h1>
        <i class="fa-solid fa-angle-down text-2xl pb-1"></i>
    </button>
    
    <div class="h-0 mb-2 transition-all overflow-auto" id="khulis-facility" style="transition: all 0.3s;" data-open="false">
    
        <div class="group rounded-2xl p-2 mb-3 text-wrap" id="khulis-facility-1"
         onmouseover="document.getElementById('khulis-facility-info-1').style.height = '80px'"
         onmouseout="document.getElementById('khulis-facility-info-1').style.height = '0px'"
         style="background-color: #090F1EFF">
         
            <h3 class=" text-2xl font-bold my-3">{facility_data.iloc[1]['FACILITY_NAME_EN']}</h3>
            
            <div class="h-0 flex overflow-hidden mb-2 justify-center" id="khulis-facility-info-1" style="display:flex;transition: all 0.3s;">
                <div class="text-center p-3 rounded-2xl">
                    <h1 class="text-xl font-bold mb-1">{facility_data.iloc[1]['Total_Occupied']}</h1>
                    <p class="text-md text-gray-400">Total Occupied</p>
                </div>
                <div class="text-center mx-2 bg-gray-900 p-3 rounded-lg">
                    <h1 class="text-xl font-bold mb-1 text-green-600">{round((facility_data.iloc[1]['Occupancy_Rate'] * 100), 2)}%</h1>
                    <p class="text-md text-gray-400">Occupancy Rate</p>
                </div>
                <div class="text-center p-3 rounded-lg">
                    <h1 class="text-xl font-bold mb-1">{facility_data.iloc[1]['Total_Vacant']}</h1>
                    <p class="text-md text-gray-400">Total Vacant</p>
                </div>
            </div>
        </div>
        
    </div>
    
    <div class="mb-2 justify-between">
        <div class="text-center p-3 rounded-2xl">
            <h1 class="text-4xl font-bold mb-1">{cluster_data.iloc[1]['Total_Occupied']}</h1>
            <p class="text-md text-gray-400">Total Occupied</p>
        </div>
        <div class="text-center p-3 rounded-2xl">
            <h1 class="text-4xl font-bold mb-1">{cluster_data.iloc[1]['Total_Vacant']}</h1>
            <p class="text-md text-gray-400">Total Vacant</p>
        </div>
        <div class="w-100 text-center mx-2 bg-gray-900 p-3 rounded-2xl">
            <h1 class="text-4xl font-bold mb-1 text-green-600">{round((cluster_data.iloc[1]['Occupancy_Rate'] * 100), 2)}%</h1>
            <p class="text-md text-gray-400">Occupancy Rate</p>
        </div>
    </div>
    
</div>


"""

qunfudah = f"""

<div class="info-card overflow-hidden qunfudah-card text-center bg-gradient-to-tr from-black to-gray-900 end-0 border border-yellow-500 text-white w-auto text-auto rounded-xl p-5" data-toggle="off" id="qunfudah-card">
    
    <!-- Close Button -->
    <div class="w-full bg-transparent border-0 justify-end text-center flex items-center">
        <button class="w-auto bg-transparent border-0 outline-none text-center"
        onmousedown="toggleCard('qunfudah', 'blur');">
            <i class="fa-solid fa-xmark text-yellow-500 text-2xl pb-1"></i>
        </button>
    </div>
    
    <!-- Main City Button -->
    <button class="w-full overflow-hidden group bg-transparent border-0 justify-center outline-none text-center flex gap-3 items-center" onmousedown="openFacility('qunfudah-facility')" id="qunfudah-button">
        <h1 class="text-4xl font-bold mb-4">Qunfudah City</h1>
        <i class="fa-solid fa-angle-down text-2xl pb-1"></i>
    </button>
    
    <!-- Facilities Container -->
    <div class="h-0 mb-2 transition-all overflow-auto" id="qunfudah-facility" style="transition: all 0.3s;" data-open="false">
        
        <!-- Facility 1 -->
        <div class="group rounded-2xl p-2 mb-3 text-wrap" id="qunfudah-facility-1" onmouseover="document.getElementById('qunfudah-facility-info-1').style.height = '80px'" onmouseout="document.getElementById('qunfudah-facility-info-1').style.height = '0px'" style="background-color: #090F1EFF">
            <h3 class="text-2xl font-bold my-3">{facility_data.iloc[10]['FACILITY_NAME_EN']}</h3>
            <div class="h-0 flex overflow-hidden mb-2 justify-center" id="qunfudah-facility-info-1" style="display:flex;transition: all 0.3s;">
                <div class="text-center p-3 rounded-2xl">
                    <h1 class="text-xl font-bold mb-1">{facility_data.iloc[10]['Total_Occupied']}</h1>
                    <p class="text-md text-gray-400">Total Occupied</p>
                </div>
                <div class="text-center mx-2 bg-gray-900 p-3 rounded-lg">
                    <h1 class="text-xl font-bold mb-1 text-green-300">{round((facility_data.iloc[10]['Occupancy_Rate'] * 100), 2)}%</h1>
                    <p class="text-md text-gray-400">Occupancy Rate</p>
                </div>
                <div class="text-center p-3 rounded-lg">
                    <h1 class="text-xl font-bold mb-1">{facility_data.iloc[10]['Total_Vacant']}</h1>
                    <p class="text-md text-gray-400">Total Vacant</p>
                </div>
            </div>
        </div>
        
        <!-- Facility 2 -->
        <div class="group rounded-2xl p-2 mb-3 text-wrap" id="qunfudah-facility-2" onmouseover="document.getElementById('qunfudah-facility-info-2').style.height = '80px'" onmouseout="document.getElementById('qunfudah-facility-info-2').style.height = '0px'" style="background-color: #090F1EFF">
            <h3 class="text-2xl font-bold my-3">{facility_data.iloc[11]['FACILITY_NAME_EN']}</h3>
            <div class="h-0 flex overflow-hidden mb-2 justify-center" id="qunfudah-facility-info-2" style="display:flex;transition: all 0.3s;">
                <div class="text-center p-3 rounded-2xl">
                    <h1 class="text-xl font-bold mb-1">{facility_data.iloc[11]['Total_Occupied']}</h1>
                    <p class="text-md text-gray-400">Total Occupied</p>
                </div>
                <div class="text-center mx-2 bg-gray-900 p-3 rounded-lg">
                    <h1 class="text-xl font-bold mb-1 text-yellow-500">{round((facility_data.iloc[11]['Occupancy_Rate'] * 100), 2)}%</h1>
                    <p class="text-md text-gray-400">Occupancy Rate</p>
                </div>
                <div class="text-center p-3 rounded-lg">
                    <h1 class="text-xl font-bold mb-1">{facility_data.iloc[11]['Total_Vacant']}</h1>
                    <p class="text-md text-gray-400">Total Vacant</p>
                </div>
            </div>
        </div>

        <!-- Facility 3 -->
        <div class="group rounded-2xl p-2 mb-3 text-wrap" id="qunfudah-facility-3" onmouseover="document.getElementById('qunfudah-facility-info-3').style.height = '80px'" onmouseout="document.getElementById('qunfudah-facility-info-3').style.height = '0px'" style="background-color: #090F1EFF">
            <h3 class="text-2xl font-bold my-3">{facility_data.iloc[12]['FACILITY_NAME_EN']}</h3>
            <div class="h-0 flex overflow-hidden mb-2 justify-center" id="qunfudah-facility-info-3" style="display:flex;transition: all 0.3s;">
                <div class="text-center p-3 rounded-2xl">
                    <h1 class="text-xl font-bold mb-1">{facility_data.iloc[12]['Total_Occupied']}</h1>
                    <p class="text-md text-gray-400">Total Occupied</p>
                </div>
                <div class="text-center mx-2 bg-gray-900 p-3 rounded-lg">
                    <h1 class="text-xl font-bold mb-1 text-green-300">{round((facility_data.iloc[12]['Occupancy_Rate'] * 100), 2)}%</h1>
                    <p class="text-md text-gray-400">Occupancy Rate</p>
                </div>
                <div class="text-center p-3 rounded-lg">
                    <h1 class="text-xl font-bold mb-1">{facility_data.iloc[12]['Total_Vacant']}</h1>
                    <p class="text-md text-gray-400">Total Vacant</p>
                </div>
            </div>
        </div>
        
    </div>
    
    <!-- Cluster Data -->
    <div class="mb-2 justify-between">
        <div class="text-center p-3 rounded-2xl">
            <h1 class="text-4xl font-bold mb-1">{cluster_data.iloc[4]['Total_Occupied']}</h1>
            <p class="text-md text-gray-400">Total Occupied</p>
        </div>
        <div class="text-center p-3 rounded-2xl">
            <h1 class="text-4xl font-bold mb-1">{cluster_data.iloc[4]['Total_Vacant']}</h1>
            <p class="text-md text-gray-400">Total Vacant</p>
        </div>
        <div class="w-100 text-center mx-2 bg-gray-900 p-3 rounded-2xl">
            <h1 class="text-4xl font-bold mb-1 text-yellow-500">{round((cluster_data.iloc[4]['Occupancy_Rate'] * 100), 2)}%</h1>
            <p class="text-md text-gray-400">Occupancy Rate</p>
        </div>
    </div>
    
</div>


"""

madinah = f"""

<div class="info-card w-auto madinah-card overflow-hidden text-center bg-gradient-to-tr from-black to-gray-900 end-0 border border-red-500 text-white w-auto text-auto rounded-xl p-5" data-toggle="off" id="madinah-card">
    
    <div class="w-full bg-transparent border-0 justify-end text-center flex items-center">
        <button class="w-auto bg-transparent border-0 outline-none text-center"
        onmousedown="toggleCard('madinah', 'blur');">
            <i class="fa-solid fa-xmark text-red-500 text-2xl pb-1"></i>
        </button>
    </div>
    
    <button class="w-full group bg-transparent border-0 justify-center outline-none text-center flex gap-3 items-center"
     onmousedown="openFacility('madinah-facility')"
     id="madinah-button">
        <h1 class="text-4xl font-bold mb-4">Madinah City</h1>
        <i class="fa-solid fa-angle-down text-2xl pb-1"></i>
    </button>
    
    <div class="h-0 mb-2 transition-all overflow-auto" id="madinah-facility" style="transition: all 0.3s;" data-open="false">
    
        <div class="group rounded-2xl p-2 mb-3 text-wrap" id="madinah-facility-1"
         onmouseover="document.getElementById('madinah-facility-info-1').style.height = '80px'"
         onmouseout="document.getElementById('madinah-facility-info-1').style.height = '0px'"
         style="background-color: #090F1EFF">
         
            <h3 class=" text-2xl font-bold my-3">{facility_data.iloc[2]['FACILITY_NAME_EN']}</h3>
            
            <div class="h-0 flex overflow-hidden mb-2 justify-center" id="madinah-facility-info-1" style="display:flex;transition: all 0.3s;">
                <div class="text-center p-3 rounded-2xl">
                    <h1 class="text-xl font-bold mb-1">{facility_data.iloc[2]['Total_Occupied']}</h1>
                    <p class="text-md text-gray-400">Total Occupied</p>
                </div>
                <div class="text-center mx-2 bg-gray-900 p-3 rounded-lg">
                    <h1 class="text-xl font-bold mb-1 text-red-500">{round((facility_data.iloc[2]['Occupancy_Rate'] * 100), 2)}%</h1>
                    <p class="text-md text-gray-400">Occupancy Rate</p>
                </div>
                <div class="text-center p-3 rounded-lg">
                    <h1 class="text-xl font-bold mb-1">{facility_data.iloc[2]['Total_Vacant']}</h1>
                    <p class="text-md text-gray-400">Total Vacant</p>
                </div>
            </div>
        </div>
    
    </div>
    
    <div class="overflow-hidden mb-2 justify-between" id="info">
        <div class="text-center p-3 rounded-2xl">
            <h1 class="text-4xl font-bold mb-1">{cluster_data.iloc[2]['Total_Occupied']}</h1>
            <p class="text-md text-gray-400">Total Occupied</p>
        </div>
        <div class="text-center p-3 rounded-2xl">
            <h1 class="text-4xl font-bold mb-1">{cluster_data.iloc[2]['Total_Vacant']}</h1>
            <p class="text-md text-gray-400">Total Vacant</p>
        </div>
        <div class="w-100 text-center mx-2 bg-gray-900 p-3 rounded-2xl">
            <h1 class="text-4xl font-bold mb-1 text-red-500">{round((cluster_data.iloc[2]['Occupancy_Rate'] * 100), 2)}%</h1>
            <p class="text-md text-gray-400">Occupancy Rate</p>
        </div>
    </div>
</div>
"""

info_cards = f"""

<!-- Info Cards -->

<!-- Makkah -->
{makkah}

<!-- Riyadh -->
{riyadh}

<!-- Kamel -->
{kamel}

<!-- Khulis -->
{khulis}

<!-- Madinah -->
{madinah}

<!-- Qunfudah -->
{qunfudah}
"""

color_dist = """
<div class="absolute color-dist bg-white items-start p-2 m-3 drop-shadow-lg rounded-xl">

    <div class="flex justify-start font-bold w-full text-black">
        <svg class="w-5 h-5 mt-2 color-wrapper">
            <!-- #b91c1c = red-700 -->
            <rect width="10px" class="color-svg" height="10px" fill="#b91c1c"></rect>
        </svg>
        <h4>100% -</h4>
    </div>

    <div class="flex justify-start font-bold w-full text-black">
        <svg class="w-5 h-5 mt-2 color-wrapper">
            <!-- #ef4444 = red-500 -->
            <rect width="10px" class="color-svg" height="10px" fill="#ef4444"></rect>
        </svg>
        <h4>80% -</h4>
    </div>

    <div class="flex justify-start font-bold w-full text-black">
        <svg class="w-5 h-5 mt-2 color-wrapper">
            <!-- #eab308 = yellow-500 -->
            <rect width="10px" class="color-svg" height="10px" fill="#eab308"></rect>
        </svg>
        <h4>60% -</h4>
    </div>

    <div class="flex justify-start font-bold w-full text-black">
        <svg class="w-5 h-5 mt-2 color-wrapper">
            <!-- #86efac = green-300 -->
            <rect width="10px" class="color-svg" height="10px" fill="#86efac"></rect>
        </svg>
        <h4>40% -</h4>
    </div>

    <div class="flex justify-start font-bold w-full text-black">
        <svg class="w-5 h-5 mt-2 color-wrapper">
            <!-- #16a34a = green-600 -->
            <rect width="10px" class="color-svg" height="10px" fill="#16a34a"></rect>
        </svg>
        <h4>20% -</h4>
    </div>

</div>
"""


# Placeholder for the map, replace the iframe src with your map URL
map_html = f"""
{styling}

<div class="h-full text-center" id="title">
    <h1 class="mb-8 font-bold fade-animation" style="font-size: 3vw">Bed monitoring - live</h1>
</div>

<div id="main-container" class=" relative w-full justify-between transition-all">
<div id="map-wrapper" class="
    relative my-auto flex justify-center transition-all aspect-[16/11] bg-gradient-to-tr from-pink-600 to-blue-700 p-5 w-full flex-1 text-white overflow-hidden"
    style="opacity: 1; transform: none;">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 870 670" fill="none" id="svgMap"
class="absolute scale-110 object-contain text-[#000001FF]">
<g id="map">
<g id="north" class="group transition ">
<g id="Group 4969">
<path id="Vector_4" class="border" d="M
280.482 131.665C280.59 131.633 280.707 131.633 280.816 131.665L292.346 135.46L298.052 133.67H308.412L323.07 137.635C323.18 137.658 323.28 137.71 323.357 137.784L331.831 146.312H337.251L343.768 143.306C343.862 143.287 343.96 143.287 344.054 143.306H346.871C347.029 143.306 347.181 143.362 347.293 143.462C347.405 143.562 347.468 143.698 347.468 143.839V148.934L350.524 151.876H359.643C359.791 151.876 359.934 151.921 360.049 152.004L363.892 154.989H368.285L376.449 149.659C376.527 149.624 376.613 149.605 376.7 149.605C376.787 149.605 376.873 149.624 376.951 149.659C377.032 149.672 377.11 149.702 377.176 149.746C377.242 149.79 377.296 149.848 377.333 149.915L389.269 170.019L397.911 176.415H408.964C409.105 176.412 409.242 176.458 409.346 176.543L420.805 185.604L425.985 189.74L428.014 187.48V178.739C428.006 178.622 428.049 178.508 428.134 178.419L440.404 164.647L453.725 141.686C453.725 141.686 453.725 141.686 453.868 141.536L475.186 124.332L418.919 120.068C418.819 120.1 418.709 120.1 418.608 120.068L310.991 43.1471L242.261 9.50505L190.482 0.359009L181.362 6.75484C181.303 6.80736 181.229 6.84424 181.148 6.86144L140.922 16.5192L136.721 30.057V37.0498L148.943 49.8414L185.349 46.6862L216.24 49.7348C216.326 49.715 216.417 49.715 216.503 49.7348L226.959 56.1307H260.858C260.979 56.1337 261.096 56.1711 261.192 56.2373L273.5 64L283.704 63.9549C283.845 63.9562 283.98 64.0015 284.086 64.0828L288.598 67.5366C288.667 67.5986 288.724 67.6707 288.765 67.7498L291.153 73.0796L303.089 81.309C303.162 81.3597 303.221 81.4243 303.262 81.4981C303.303 81.5718 303.326 81.6529 303.328 81.7353V84.1231C303.326 84.2133 303.299 84.3017 303.249 84.38C303.199 84.4583 303.127 84.5239 303.041 84.5708L254.484 112.371V126.314C254.521 126.426 254.521 126.544 254.484 126.655L247.322 134.33L252.097 136.974L280.482 131.665Z" 
fill="currentColor" stroke="black"></path>

<path id="Vector_5" d="M186.4 155.972L206.621 147.828H206.859H211.419L241.618 134.034C241.712 134.015 241.81 134.015 241.904 134.034H245.986L256.5 126.5L254.5 113C254.499 112.909 254.45 112.579 254.5 112.5C254.55 112.421 256.412 111.883 256.5 111.838L307.5 86L303 76L291.5 73C291.404 72.9471 291.027 71.5975 291 71.5L288.5 67L283.5 57.2626L273.5 64C274 64 271.609 62.031 271.5 62L260.5 55L227.5 55.5C227.166 53.1749 224.609 53.531 224.5 53.5L214.5 48.5L172.5 32L150 47C150 45.4698 148.091 48.5333 148 48.5C147 47 139 37.2436 148.133 50.7602L141 38C144.472 37.4152 138.463 35.1113 138.5 35L138 29.8458C137.987 29.7968 139.487 29.8949 139.5 29.8458L141 16.5L100.913 26.0936L141.162 66.2168C141.222 66.2734 141.267 66.3406 141.296 66.4141C141.325 66.4876 141.336 66.5656 141.329 66.6432C141.292 66.7993 141.19 66.9368 141.043 67.0269L127.865 74.2542L120.345 87.6002C120.308 87.6723 120.251 87.7352 120.18 87.7835C120.11 87.8318 120.027 87.864 119.939 87.8773L89.1196 92.8021L78.1621 108.792C78.1364 108.855 78.0854 108.909 78.0189 108.941L60.8545 120.155C60.7959 120.229 60.7164 120.287 60.6241 120.325C60.5318 120.362 60.4301 120.377 60.3293 120.368L15.1862 113.972L10.5 133.5L26.5 134.5L32 131.5C32.0869 131.434 32.386 130.503 32.5 130.5L49.5 129H50.5L61 131.5C61.1186 131.531 62.4155 131.919 62.5 132L76.5 146.5L94.5 143C94.6168 142.969 95.8832 142.469 96 142.5L105 148.5L117.5 150.5L122 139.5C122.061 139.396 122.389 138.064 122.5 138L127 135.5C127 136.5 130 134.5 130.74 131.709C130.844 131.71 128.911 133.953 129 134C129.089 134.047 131 133 131.249 131.979C131.3 132.059 130 133.407 130 133.5L125 158.5L135.528 161.856H148.5H159.5C159.601 161.855 158.68 160.139 162.5 158.5C161.68 161.639 157.968 164.807 163 160.5L162 165L169.5 167.5L176.995 159.297C177.082 159.255 177.181 159.232 177.281 159.232C177.381 159.232 177.48 159.255 177.568 159.297L182.342 161.856L185.971 156.27C186.016 156.197 186.078 156.133 186.151 156.082C186.225 156.03 186.31 155.993 186.4 155.972Z" 
fill="currentColor" stroke="black"></path>

<path id="Vector_6" d="M
220.465 212.041L230.396 201.382L219.821 194.986C219.708 194.903 219.624 194.791 219.582 194.666L214.545 176.694L200.484 166.524L182.58 163.007C182.553 163.017 182.525 163.022 182.496 163.022C182.467 163.022 182.439 163.017 182.412 163.007L177.304 160.299L170.596 163.284C170.51 163.306 170.419 163.306 170.333 163.284H166.871C166.765 163.282 166.66 163.255 166.568 163.207C166.476 163.158 166.4 163.089 166.346 163.007L163.219 158.274H156.391L137.293 156.483C137.213 156.474 137.136 156.45 137.066 156.413C136.996 156.377 136.935 156.328 136.887 156.27L130.275 148.488C130.238 148.384 130.238 148.272 130.275 148.168V133.159L122.134 137.423L118.124 145.418C118.077 145.513 118 145.594 117.903 145.651C117.805 145.708 117.691 145.738 117.574 145.738H106.88H106.665L95.7311 142.071L77.1104 146.335C77.003 146.359 76.8903 146.355 76.785 146.325C76.6796 146.295 76.5856 146.239 76.5136 146.164L62.5004 131.369L50.397 128.512L32.3732 130.388L27.3838 133.799C27.3196 133.823 27.2506 133.835 27.1809 133.835C27.1112 133.835 27.0422 133.823 26.978 133.799L10.482 133.159L9.24064 138.148V146.42C9.25175 146.491 9.25175 146.563 9.24064 146.633L0.216797 163.689L2.93827 166.695L7.71279 163.348C7.7861 163.312 7.86815 163.294 7.95152 163.294C8.03489 163.294 8.11694 163.312 8.19025 163.348L25.4263 166.098C25.5042 166.112 25.5782 166.14 25.6438 166.181C25.7094 166.221 25.7653 166.273 25.8082 166.332L38.7472 183.793C38.7819 183.89 38.7819 183.994 38.7472 184.092V188.078L44.5721 194.474H46.0044C46.1113 194.476 46.2158 194.502 46.3078 194.551C46.3998 194.6 46.4762 194.669 46.5296 194.751L49.9434 200.401C49.9649 200.485 49.9649 200.573 49.9434 200.657V204.921L59.4925 213.001C59.5541 213.048 59.6033 213.107 59.6363 213.173C59.6693 213.24 59.6854 213.312 59.6834 213.384V216.305L69.877 227.732C69.9721 227.825 70.0234 227.948 70.0203 228.074V229.886L79.5693 245.086H85.1555C85.326 245.087 85.4891 245.149 85.6091 245.257C85.667 245.31 85.7101 245.374 85.735 245.444C85.7599 245.515 85.7658 245.589 85.7523 245.662L84.9645 253.166V255.917L87.877 258.219H90.2642C90.3399 258.216 90.4154 258.228 90.4855 258.254C90.5555 258.28 90.6185 258.319 90.6701 258.368L95.6594 262.632L95.8027 262.824L99.3836 271.075L107.906 281.735C107.944 281.838 107.944 281.95 107.906 282.054V285.402L109.267 295.187C109.277 295.327 109.226 295.465 109.124 295.571C109.027 295.674 108.891 295.742 108.742 295.763L105.59 296.083L105.901 298.428L115.617 308.49L116.524 302.564C116.547 302.438 116.62 302.323 116.729 302.241C116.839 302.159 116.978 302.114 117.121 302.116H125.572L129.391 297.66C129.453 297.585 129.537 297.527 129.635 297.493C129.732 297.459 129.838 297.45 129.941 297.468L137.389 298.321L140.421 295.4V270.904H135.646C135.513 270.907 135.382 270.868 135.278 270.794C135.173 270.72 135.101 270.616 135.073 270.499L132.686 261.14L122.707 252.612C122.648 252.563 122.6 252.504 122.568 252.438C122.535 252.372 122.517 252.301 122.516 252.228V248.498L115.736 244.809H113.492L110.795 246.43C110.71 246.471 110.616 246.492 110.52 246.492C110.424 246.492 110.33 246.471 110.246 246.43C110.156 246.402 110.076 246.354 110.013 246.29C109.95 246.227 109.907 246.15 109.888 246.067L106.14 233.275C106.105 233.209 106.087 233.136 106.087 233.062C106.087 232.989 106.105 232.916 106.14 232.849L109.649 228.436V225.345L103.609 223.213C103.538 223.224 103.465 223.224 103.394 223.213L98.2377 218.714C98.1309 218.609 98.0714 218.472 98.0706 218.331V202.128H90.9088C90.7505 202.128 90.5987 202.072 90.4868 201.972C90.3749 201.872 90.312 201.736 90.312 201.595V198.525C90.3087 198.415 90.3436 198.306 90.412 198.215C90.4804 198.123 90.5789 198.053 90.694 198.013L109.792 191.98C109.954 191.926 110.132 191.926 110.293 191.98L119.556 196.585L128.532 192.086C128.634 192.065 128.74 192.065 128.842 192.086H133.211C133.369 192.086 133.521 192.142 133.633 192.242C133.745 192.342 133.808 192.478 133.808 192.619V195.54L140.134 205.944H149.468C149.627 205.944 149.778 206 149.89 206.1C150.002 206.2 150.065 206.336 150.065 206.477V210.101L153.956 212.425C154.04 212.473 154.108 212.539 154.154 212.618C154.2 212.696 154.222 212.784 154.219 212.873V216.518H155.818L162.694 212.425C162.78 212.378 162.879 212.353 162.98 212.353C163.081 212.353 163.18 212.378 163.267 212.425L170.428 215.367V210.677C170.428 210.535 170.491 210.4 170.603 210.3C170.715 210.2 170.867 210.144 171.025 210.144H173.222C173.347 210.146 173.469 210.181 173.571 210.246C173.673 210.31 173.751 210.401 173.794 210.506L175.442 215.09L188.595 221.891L213.447 218.714C213.543 218.702 213.642 218.712 213.733 218.741C213.825 218.771 213.907 218.82 213.972 218.885L217.147 222.168L220.561 212.148C220.526 212.115 220.494 212.079 220.465 212.041Z" 
fill="currentColor" stroke="black"></path>

<path id="Vector_7" d="M295.902 261.438L303.66 259.69L301.536 252.079C301.499 251.984 301.498 251.881 301.532 251.785C301.567 251.689 301.635 251.605 301.727 251.546L305.117 249.073C305.21 249.022 305.317 248.995 305.427 248.995C305.536 248.995 305.644 249.022 305.737 249.073L312.04 251.589V240.929C312.039 240.825 312.073 240.723 312.137 240.636C312.2 240.549 312.291 240.48 312.398 240.439L317.483 238.307C317.568 238.285 317.659 238.285 317.745 238.307H320.658L321.565 233.254C321.583 233.12 321.66 232.997 321.78 232.913L344.554 216.774H344.697L355.75 212.51L359.856 205.816C359.917 205.73 359.999 205.657 360.095 205.603L381.58 194.943C381.675 194.924 381.773 194.924 381.867 194.943H386.641C386.717 194.942 386.792 194.954 386.862 194.98C386.932 195.006 386.995 195.044 387.047 195.092L398.291 204.473H409.631L412.997 200.486L412.591 200.252C412.509 200.202 412.442 200.136 412.396 200.057C412.351 199.979 412.327 199.892 412.328 199.804V193.493C412.334 193.365 412.394 193.243 412.495 193.152L422.5 183.5L407.5 173L398.5 176C397.138 174.975 397.107 174.581 397 174.5L390 169.5L389 166.5L376.5 148.5L368.5 154.5C367.596 153.422 365.617 154.533 365.5 154.5L364 152C363.594 150.922 361.5 144.55 361.5 152L357.5 149.533L351.5 150C351.329 149.999 347.075 143.649 349 149.149L347.5 148.5C347.5 148.5 348.5 148.5 347.5 146.5C348.5 145.5 348 143 347.5 142L346.5 142.5H342L337.5 144L332 143L331.5 145C331.419 145.002 331.074 145.53 331 145.5C330.926 145.471 328.053 139.055 328 139L321 136L306 133L294 128L293 135C292.594 130.494 282.37 126.994 289.5 133.5L277 128L254.5 134.5C254.355 134.553 249.5 119.98 249.5 128L235 133.5L213.5 146C216.448 144.057 209.988 141.192 208.5 146L204.5 148L172.5 150L177 170H193C193.097 170.013 203 177.084 203 170L213.5 176C213.599 176.069 213.975 176.39 214 176.5L217.5 192.5L219.5 195C219.567 195.041 218.174 194.165 224 198C219.674 196.665 227.601 200.46 229.5 201C225.851 200.795 221.101 200.054 228 201.5L217.886 208L217 219.5L217.886 228.905C217.885 229.024 217.834 229.138 217.743 229.225L214.234 233.19L216.048 234.469H221.801C221.885 234.468 221.968 234.484 222.045 234.515C222.122 234.546 222.19 234.591 222.244 234.648C222.299 234.705 222.339 234.772 222.361 234.844C222.384 234.917 222.388 234.992 222.374 235.066L220.178 254.083L222.565 259.413C222.587 259.476 222.587 259.543 222.565 259.605V274.06L227.34 276.042L239.61 272.482H248.92L256.918 265.319C256.974 265.269 257.041 265.229 257.115 265.204C257.189 265.178 257.268 265.166 257.347 265.169H268.591L282.557 267.813L295.902 261.438Z"
fill="currentColor" stroke="black"></path></g>
</g>

<g id="east" class="group relative transition border">
<path id="Vector" 
d="M438.901 192.193V197.736L452.031 204.43H458.142C458.223 204.428 458.304 204.443 458.378 204.472C458.453 204.502 458.519 204.546 458.572 204.601L468.813 214.834H480.749C480.86 214.813 480.974 214.813 481.084 214.834L494.309 222.999H505.362C505.521 223 505.674 223.053 505.792 223.149L515.102 231.676L533.365 237.88C533.48 237.915 533.581 237.981 533.654 238.068C533.726 238.156 533.767 238.262 533.771 238.371V298.598L554.874 313.522C554.874 313.522 554.874 313.522 554.993 313.628L566.524 328.232C566.598 328.318 566.64 328.422 566.643 328.531V349.189L544.203 512.155L533.938 586.517L530.834 609.18L532.529 608.263L538.712 593.851C538.696 593.81 538.696 593.764 538.712 593.723L562.394 565.944C562.446 565.883 562.511 565.833 562.585 565.795L599.85 548.227H600.041L690.566 537.269L719.619 531.833L842.586 492.498L870.231 410.952L851.61 383.535L843.78 389.931C843.713 389.984 843.633 390.024 843.546 390.046C843.459 390.068 843.368 390.072 843.279 390.058L743.014 373.173C742.872 373.152 742.744 373.083 742.656 372.982L701.476 326.612C701.4 326.511 701.359 326.392 701.356 326.271V321.005L694.314 317.53L690.613 319.662C690.525 319.713 690.421 319.74 690.315 319.74C690.209 319.74 690.106 319.713 690.017 319.662C689.923 319.621 689.843 319.557 689.788 319.478C689.734 319.399 689.705 319.307 689.706 319.214V314.95C689.672 314.853 689.672 314.749 689.706 314.652L695.913 306.124H694.529L692.141 309.407C692.088 309.481 692.013 309.542 691.925 309.583C691.837 309.624 691.739 309.645 691.64 309.642H690.184C690.026 309.642 689.874 309.585 689.762 309.485C689.65 309.385 689.587 309.25 689.587 309.109V306.06H686.269L683.714 308.192C683.664 308.243 683.601 308.282 683.531 308.308C683.46 308.334 683.384 308.345 683.308 308.341H677.698C677.606 308.341 677.514 308.322 677.432 308.285C677.349 308.248 677.277 308.194 677.221 308.128L670.656 300.282H667.815C667.699 300.283 667.585 300.253 667.487 300.196C667.389 300.139 667.313 300.058 667.266 299.962L661.919 288.173H660.128C659.97 288.173 659.818 288.117 659.706 288.017C659.594 287.917 659.531 287.781 659.531 287.64V285.956L655.831 272.375H650.77C650.669 272.376 650.569 272.353 650.481 272.308C650.393 272.263 650.32 272.198 650.269 272.119L641.842 259.711C641.784 259.632 641.754 259.539 641.754 259.445C641.754 259.35 641.784 259.258 641.842 259.178C641.887 259.094 641.958 259.024 642.047 258.975C642.136 258.926 642.239 258.9 642.343 258.901H643.37L641.317 256.343C641.282 256.246 641.282 256.142 641.317 256.044V251.077L636.208 249.116C636.101 249.074 636.01 249.005 635.947 248.918C635.883 248.831 635.849 248.729 635.85 248.625V241.377C635.849 241.273 635.883 241.171 635.947 241.084C636.01 240.997 636.101 240.928 636.208 240.886C636.299 240.83 636.407 240.8 636.518 240.8C636.629 240.8 636.737 240.83 636.829 240.886L641.46 244.319H642.821L644.921 241.398V232.678L637.64 229.544C637.542 229.501 637.458 229.435 637.399 229.352C637.34 229.269 637.308 229.173 637.306 229.075V220.782C637.305 220.691 637.331 220.602 637.381 220.524C637.432 220.445 637.505 220.38 637.592 220.334C637.679 220.287 637.778 220.262 637.879 220.262C637.98 220.262 638.079 220.287 638.165 220.334L641.866 221.997L634.417 214.322H630.622C630.546 214.325 630.471 214.313 630.4 214.287C630.33 214.262 630.267 214.223 630.216 214.173L616.895 202.703H609.948C609.844 202.702 609.742 202.678 609.65 202.633C609.559 202.588 609.481 202.525 609.423 202.447L601.975 191.788H600.423C600.265 191.788 600.113 191.731 600.001 191.632C599.889 191.532 599.826 191.396 599.826 191.255V189.848C599.826 189.706 599.889 189.571 600.001 189.471C600.113 189.371 600.265 189.315 600.423 189.315H606.176V188.014L599.014 186.01H597.057L588.343 183.75C588.221 183.715 588.114 183.647 588.037 183.555C587.96 183.464 587.917 183.353 587.914 183.239V181.256H586.338C586.18 181.256 586.028 181.2 585.916 181.1C585.804 181 585.741 180.864 585.741 180.723V175.798C585.741 175.657 585.804 175.521 585.916 175.421C586.028 175.321 586.18 175.265 586.338 175.265H587.579L585.407 171.236C585.394 171.158 585.394 171.079 585.407 171.001V167.974H581.229C581.113 167.974 580.999 167.944 580.901 167.887C580.804 167.83 580.727 167.749 580.68 167.654L578.293 162.516C578.267 162.447 578.267 162.372 578.293 162.303V158.615L574.402 154.884C574.347 154.837 574.305 154.78 574.276 154.718C574.247 154.656 574.233 154.589 574.235 154.521V148.083L570.773 146.548H542.341C542.248 146.546 542.158 146.526 542.075 146.489C541.993 146.452 541.92 146.4 541.863 146.335L537.089 140.749C537.011 140.657 536.969 140.544 536.969 140.429V133.713L531.097 127.723L491.755 123.864L489.368 125.271C489.243 125.303 489.11 125.303 488.986 125.271L476.811 124.354L454.704 142.156L441.431 165.16L429.232 178.847V185.648L438.614 191.681C438.716 191.729 438.798 191.804 438.85 191.896C438.901 191.987 438.919 192.091 438.901 192.193Z" 
fill="currentColor" stroke="black">
</path>

<g id="middle" class="group transition ">

<!-- Riyadh -->
<path class="border id="Vector_12" d="M413.643 199.359L414.312 199.764L423.503 205.285C423.583 205.336 423.649 205.403 423.695 205.481C423.74 205.559 423.764 205.645 423.765 205.733V209.997C423.769 210.086 423.746 210.173 423.7 210.252C423.654 210.33 423.586 210.397 423.503 210.445L414.24 215.945L410.803 221.446C410.745 221.523 410.667 221.587 410.575 221.631C410.484 221.676 410.382 221.7 410.277 221.701H405.503V234.941L417.869 249.459C417.944 249.561 417.986 249.679 417.988 249.8V251.186C417.988 251.328 417.925 251.463 417.813 251.563C417.701 251.663 417.55 251.719 417.391 251.719H416.436V254.896L419.492 258.179C419.583 258.274 419.634 258.395 419.635 258.52V266.579C419.635 266.72 419.573 266.856 419.461 266.956C419.349 267.056 419.197 267.112 419.039 267.112H388.697L383.922 274.254C383.896 274.311 383.855 274.363 383.803 274.403L377.023 279.328C376.95 279.391 376.859 279.435 376.76 279.456L362.222 282.099L352.53 290.265V295.637H353.866C353.953 295.638 354.039 295.655 354.117 295.689C354.195 295.722 354.265 295.77 354.32 295.829C354.36 295.898 354.381 295.975 354.381 296.053C354.381 296.131 354.36 296.208 354.32 296.277L352.864 302.012C352.836 302.128 352.764 302.233 352.659 302.306C352.554 302.38 352.424 302.419 352.291 302.417H327.01H326.771L317.222 298.643L311.397 304.058V309.367C311.387 309.522 311.31 309.667 311.182 309.772L307.339 312.714L305.954 331.774V339.065L311.516 344.032C311.578 344.08 311.627 344.139 311.66 344.205C311.693 344.271 311.709 344.344 311.707 344.416V348.211L315.575 357.549L324.217 373.24H342.599C342.678 373.237 342.757 373.249 342.831 373.274C342.905 373.3 342.972 373.339 343.028 373.389L348.805 378.506C348.861 378.552 348.905 378.608 348.933 378.671C348.962 378.733 348.976 378.801 348.973 378.868V388.547L353.747 389.997L357.614 388.675H357.829H366.137C366.291 388.675 366.439 388.728 366.551 388.824C366.662 388.919 366.728 389.049 366.734 389.187L368.62 415.922C368.629 415.986 368.623 416.052 368.603 416.114C368.582 416.176 368.547 416.234 368.5 416.284L365.564 419.674V431.229C365.576 431.285 365.576 431.343 365.564 431.399L363.63 436.431L374.827 452.058L383.516 458.752C383.583 458.785 383.634 458.838 383.659 458.902L388.1 466.449L392.11 468.879C392.192 468.928 392.259 468.995 392.305 469.073C392.351 469.152 392.374 469.239 392.373 469.327V473.228C392.37 473.343 392.328 473.454 392.254 473.548L387.813 478.814L385.426 488.237L410.994 512.008L429.232 522.37L469.648 520.813L543.152 511.859L565.545 349.362V328.938L554.062 314.377L532.792 299.453C532.722 299.406 532.667 299.345 532.629 299.274C532.592 299.204 532.574 299.126 532.577 299.048V238.928L514.553 232.809C514.466 232.792 514.389 232.746 514.338 232.681L505.123 224.26H494.118C493.997 224.257 493.88 224.219 493.784 224.153L480.487 215.903H468.55C468.38 215.901 468.217 215.84 468.097 215.732L457.855 205.499H451.84C451.739 205.529 451.63 205.529 451.529 205.499L437.946 198.612C437.859 198.561 437.788 198.491 437.738 198.409C437.688 198.328 437.661 198.236 437.659 198.143V192.558L429.208 187.143V187.761C429.211 187.887 429.16 188.009 429.065 188.102L426.511 190.937C426.405 191.042 426.261 191.11 426.105 191.129C426.029 191.132 425.954 191.12 425.884 191.094C425.814 191.069 425.751 191.03 425.699 190.98L420.495 186.844L413.643 193.709V199.359Z"
fill="#fde047" stroke="black"></path>
<path id="Vector_13" d="M410.42 205.155C410.369 205.225 410.298 205.282 410.214 205.32C410.13 205.357 410.036 205.374 409.943 205.368H398.006C397.858 205.374 397.712 205.328 397.601 205.24L386.357 195.838H382.06L360.765 206.498L356.611 213.213C356.546 213.317 356.446 213.399 356.325 213.448L345.176 217.712L322.641 233.659L321.686 238.967C321.668 239.092 321.6 239.206 321.495 239.288C321.389 239.371 321.253 239.416 321.113 239.415H317.795L313.163 241.355V252.463C313.162 252.55 313.138 252.637 313.092 252.715C313.047 252.793 312.981 252.86 312.901 252.91C312.812 252.951 312.714 252.973 312.614 252.973C312.514 252.973 312.416 252.951 312.328 252.91L305.524 250.203L302.707 252.335L304.88 260.138C304.901 260.205 304.907 260.275 304.896 260.345C304.886 260.414 304.86 260.48 304.82 260.54C304.779 260.6 304.726 260.652 304.662 260.693C304.599 260.734 304.526 260.762 304.45 260.777L296.261 262.611L284.325 268.324L291.893 269.603C292.023 269.628 292.14 269.693 292.223 269.786C292.306 269.88 292.349 269.996 292.346 270.115V285.934L300.177 288.556C300.248 288.579 300.314 288.615 300.368 288.663C300.421 288.711 300.462 288.769 300.487 288.834L304.402 296.125C304.423 296.202 304.423 296.282 304.402 296.359V300.069L308.126 303.992H311.5L315 306.5C314.998 306.433 311.471 304.062 311.5 304C311.529 303.938 314.869 304.648 312.5 303.5L317.078 300.5C317.164 300.423 321.567 301.286 321.686 301.263C321.805 301.24 316.965 297.343 317.078 297.383L326.5 304.5L350 302.5L353 303L354.5 300C354.342 300 354.612 297.6 354.5 297.5C354.388 297.4 357 296.757 357 296.615L354.5 293.5C354.498 293.427 352.356 294.269 352.5 291C352.533 290.934 353.938 290.547 354 290.5L361 286C361.079 285.933 362.5 287.031 362.5 282L376 283.5L382.06 278.259L392.5 276.5C392.553 276.423 388.117 270.557 388.5 268C390.617 270.057 391.329 268.127 389 267.5L415.393 269H424L423 261C422.905 260.907 422.997 259.126 423 259L418.418 256C418.418 255.859 415.282 250.736 415.393 250.636C418.418 256 419.5 252.964 415.815 250.48L415.219 252.964L423 254L412.5 240C418.038 239.68 413.658 235.578 409.943 235.258L408 225C408 224.859 406.388 222.6 406.5 222.5C406.612 222.4 408.842 225 409 225H410.42L413.5 219.5C413.667 223.368 418.609 223.212 416.77 217.712L423 213.213L429.5 206.498L415.815 199L410.42 205.155Z"
fill="currentColor" stroke="black"></path>


</g>

<g id="west" class="group transition  text-secondary-4">

<!-- Madinah -->
<path id="Vector_2" d="
M306.215 311.923L310.059 308.981V305.037H307.934C307.847 305.036 307.762 305.018 307.684 304.985C307.605 304.952 307.536 304.904 307.48 304.845L303.422 300.581C303.347 300.472 303.306 300.347 303.303 300.218V296.466L299.555 289.452L291.581 286.787C291.466 286.752 291.365 286.687 291.292 286.599C291.22 286.511 291.179 286.406 291.176 286.297V270.52L282.486 268.879L268.425 266.193H257.539L249.566 273.356C249.444 273.445 249.293 273.498 249.136 273.505H239.849L227.436 277.108C227.358 277.131 227.274 277.131 227.197 277.108L221.778 274.976C221.671 274.935 221.58 274.866 221.517 274.779C221.453 274.692 221.419 274.59 221.42 274.486V259.797L219.033 254.446C219.009 254.362 219.009 254.274 219.033 254.19L221.205 235.62H215.929C215.804 235.651 215.672 235.651 215.547 235.62L213.16 233.894C213.034 233.803 212.949 233.674 212.921 233.531C212.864 233.401 212.864 233.256 212.921 233.126L216.693 228.862V223.66L213.112 219.865L188.38 223.042C188.257 223.085 188.121 223.085 187.998 223.042L174.462 216.049C174.338 215.98 174.245 215.875 174.2 215.751L172.529 211.274H171.359V216.305C171.362 216.394 171.34 216.481 171.294 216.56C171.248 216.638 171.18 216.705 171.096 216.753C171.008 216.794 170.91 216.815 170.81 216.815C170.71 216.815 170.612 216.794 170.523 216.753L162.98 213.576L156.248 217.606C156.137 217.625 156.024 217.625 155.913 217.606H153.717C153.559 217.606 153.407 217.549 153.295 217.449C153.183 217.349 153.12 217.214 153.12 217.073V213.171L149.229 210.847C149.147 210.803 149.08 210.74 149.034 210.665C148.988 210.59 148.965 210.506 148.966 210.421V207.031H139.847C139.739 207.034 139.633 207.009 139.54 206.96C139.447 206.911 139.371 206.84 139.322 206.754L132.757 195.966C132.735 195.882 132.735 195.795 132.757 195.71V193.173H129.057L120.009 197.821C119.921 197.864 119.823 197.887 119.723 197.887C119.622 197.887 119.524 197.864 119.436 197.821L110.102 193.195L91.6006 199.015V201.147H98.7624C98.9207 201.147 99.0725 201.203 99.1844 201.303C99.2963 201.403 99.3592 201.539 99.3592 201.68V218.202L104.134 222.466L110.46 224.598C110.571 224.637 110.667 224.704 110.735 224.791C110.803 224.879 110.84 224.982 110.842 225.089V228.713C110.88 228.817 110.88 228.929 110.842 229.033L107.38 233.297L110.818 245.022L112.967 243.743C113.076 243.717 113.191 243.717 113.301 243.743H115.903C116.005 243.721 116.111 243.721 116.213 243.743L123.375 247.645C123.461 247.692 123.533 247.757 123.583 247.836C123.633 247.914 123.66 248.002 123.661 248.092V251.823L133.592 260.351C133.679 260.425 133.738 260.522 133.76 260.628L136.147 269.71H140.921C141.08 269.71 141.231 269.766 141.343 269.866C141.455 269.966 141.518 270.102 141.518 270.243V295.379C141.52 295.446 141.506 295.513 141.477 295.576C141.448 295.638 141.405 295.694 141.351 295.741L137.961 299.025C137.896 299.089 137.813 299.136 137.721 299.162C137.629 299.188 137.53 299.192 137.436 299.174L130.035 298.321L126.24 302.734C126.183 302.799 126.111 302.852 126.028 302.889C125.945 302.926 125.855 302.946 125.762 302.947H117.622L116.667 309.343L118.863 311.603C118.956 311.706 119.006 311.834 119.006 311.965V315.099L122.038 318.212L125.547 319.299L126.693 317.487C126.742 317.421 126.806 317.365 126.879 317.321C126.953 317.277 127.036 317.246 127.123 317.231C127.214 317.217 127.307 317.222 127.395 317.249C127.483 317.275 127.562 317.32 127.624 317.381L133.545 322.455H137.985C138.11 322.421 138.242 322.421 138.367 322.455L160.115 338.423C160.243 338.528 160.32 338.673 160.33 338.828V341.216L164.173 348.486H166.561C166.692 348.49 166.818 348.532 166.921 348.605C167.024 348.678 167.098 348.778 167.133 348.891L169 354.5L179.5 353C180 353.5 179 353 179.5 353C179.748 353.248 179.5 353.5 180 354L190 365L200 365.5C200.158 365.5 199.888 368.4 200 368.5C200.112 368.6 201 368.359 201 368.5L202 369.5L205.5 368.5L214.5 366H220C220.158 366 220.5 367 220.5 367C220.5 367 220 370.5 220.5 370L219.5 373C219.514 373.056 216.58 376.551 219.5 374L216.625 380.738L225 382C225.116 382.035 222.017 385.262 223.5 385.5C223.517 388.762 229.5 389.5 226.6 381.04L224 391.5L232.5 392L240 387.5C240.145 387.447 241.355 387.947 241.5 388L251 390L258 381L279 367.5L282.5 366.5L286 362.5L285 357.5L277 356C276.92 355.949 276.641 355.886 276.5 356C277.629 355.109 277.001 355.088 277 355V354.5C277 355 277.002 354.405 277 354.5C277.054 354.418 279 354.5 279 353.5L295.5 346L298 338L296 333.5C295.968 333.436 294.015 333.045 294.014 332.974C294.012 332.904 293.928 333.244 293.957 333.178C293.986 333.113 294.919 334.053 294.5 333.5C294.555 333.45 295.428 333.528 295.5 333.5L297.219 333.178C297.297 333.158 298.098 333.483 298.125 332.593L304.5 333.178L306.024 312.307C306.029 312.161 306.098 312.023 306.215 311.923Z"
 fill="#ef4444" stroke="black"></path>
 
 
 <!-- Makkah -->
 <path id="Vector_3" d="M
 296.045 558.781 L298.05 552.236 L293.276 542.151H283.034C282.872 542.145 282.719 542.084 282.605 541.981L280.217 539.849C280.118 539.748 280.059 539.621 280.05 539.486V524.563C280.05 
 524.467 280.079 524.373 280.133 524.29C280.188 524.208 280.266 524.14 280.361 524.094C280.456 524.047 280.562 524.023 280.671 524.023C280.779 524.023 280.886 524.047 280.981 
 524.094L284.276 526.098L290.315 522.751C290.418 522.732 290.523 522.732 290.626 522.751H299.578L301.965 516.163L298.026 509.447C297.998 509.39 297.983 509.329 297.983 509.266C297.983 
 509.204 297.998 509.142 298.026 509.085L299.888 501.41L294.78 500.429L294.398 501.239C294.355 501.339 294.28 501.424 294.182 501.485C294.084 501.546 293.968 501.579 293.849 501.581H286.687L281.459 
 510.513V517.357C281.459 517.498 281.396 517.634 281.284 517.734C281.172 517.834 281.02 517.89 280.862 517.89H271.17C270.999 517.889 270.836 517.828 270.716 517.719L263.005 510.407C262.91 510.314 262.859 
 510.192 262.862 510.066L261.453 493.01H256.942C256.783 493.01 256.631 492.954 256.52 492.854C256.408 492.754 256.345 492.618 256.345 492.477V487.723C256.346 487.651 256.363 487.579 256.396 
 487.514C256.429 487.448 256.476 487.388 256.536 487.339L261.788 483.075C261.9 482.986 262.043 482.934 262.194 482.926H269.618L274.918 471.477V463.227C274.911 463.094 274.962 462.964 275.061 
 462.864L276.971 461.01C277.019 460.948 277.083 460.898 277.158 460.865C277.233 460.831 277.316 460.815 277.4 460.818H280.838C280.957 460.819 281.073 460.852 281.171 460.913C281.269 460.974 
 281.344 461.06 281.387 461.159L284.729 467.874H289.337L306.716 464.655C306.794 464.634 306.877 464.634 306.955 464.655L314.331 477.447H318.151L333.931 464.208C333.986 464.146 334.061 464.102 
 334.146 464.08L339.374 462.587L344.578 458.323L344.864 458.195L354.008 456.362H360.071C360.165 456.343 360.263 456.343 360.358 456.362L362.745 457.492L373.344 451.586L362.267 436.13C362.226 436.057 
 362.204 435.977 362.204 435.895C362.204 435.814 362.226 435.733 362.267 435.661L364.249 430.48V418.84C364.247 418.78 364.258 418.721 364.283 418.666C364.307 418.611 364.345 418.561 364.392 418.52L367.305 
 415.13L365.443 389.078H357.827L353.84 390.442C353.777 390.469 353.708 390.483 353.638 390.483C353.567 390.483 353.498 390.469 353.435 390.442L348.111 388.779C347.995 388.744 347.894 388.679 347.822 
 388.591C347.749 388.503 347.709 388.398 347.705 388.289V378.972L342.286 374.176H323.785C323.672 374.173 323.562 374.144 323.466 374.092C323.369 374.039 323.29 373.965 323.236 373.877L314.427 
 357.845L310.464 348.486C310.452 348.422 310.452 348.357 310.464 348.294V344.605L304.878 339.638C304.822 339.588 304.778 339.528 304.749 339.462C304.72 339.396 304.707 339.325 304.711 
 339.254V332.261H298.241L295.472 333.349L297.024 336.44C297.059 336.544 297.059 336.656 297.024 336.76L295.353 344.989C295.334 345.066 295.297 345.139 295.243 345.202C295.189 345.264 295.121 345.315 
 295.042 345.352L276.541 354.626V355.969L283.894 360.233C283.985 360.274 284.061 360.339 284.112 360.418C284.163 360.498 284.187 360.589 284.18 360.68V363.196C284.182 363.303 284.146 363.408 284.078 
 363.496C284.009 363.584 283.911 363.651 283.798 363.686L276.302 366.245L257.013 381.168L250.83 388.993C250.772 389.062 250.696 389.117 250.609 389.154C250.522 389.192 250.425 389.209 250.329 
 389.206H250.186L240.183 386.669L231.637 390.933C231.543 390.954 231.444 390.954 231.35 390.933H226.003C225.844 390.933 225.693 390.876 225.581 390.776C225.469 390.677 225.406 390.541 
 225.406 390.4V381.573L218.244 379.228C218.101 379.172 217.983 379.074 217.91 378.951C217.85 378.821 217.85 378.676 217.91 378.546L220.44 372.321V365.498H215.188L204.159 368.334H200.745C200.587 
 368.334 200.435 368.278 200.323 368.178C200.212 368.078 200.149 367.942 200.149 367.801V364.987H190.433C190.342 364.989 190.252 364.973 190.169 364.94C190.086 364.907 190.013 364.857 189.955 
 364.795L179.165 352.749L168.685 353.858L170.594 360.147L173.793 364.411C173.827 364.508 173.827 364.612 173.793 364.71V369.848L185.73 387.351C185.75 387.442 185.75 387.537 185.73 387.628V401.315C185.73 
 401.457 185.667 401.592 185.555 401.692C185.443 401.792 185.291 401.848 185.133 401.848H184.464V408.244L186.685 429.969H188.642C188.8 429.969 188.952 430.025 189.064 430.125C189.176 430.225 189.239 430.36 
 189.239 430.501V437.196C189.239 437.337 189.176 437.473 189.064 437.573C188.952 437.673 188.8 437.729 188.642 437.729H186.255L194.73 454.55L212.085 476.488L245.339 493.543C245.434 493.592 245.509 
 493.667 245.554 493.756L250.019 501.389H255.915C256.073 501.389 256.225 501.445 256.337 501.545C256.449 501.645 256.512 501.78 256.512 501.922V508.659L260.618 511.857H262.265C262.423 
 511.857 262.575 511.913 262.687 512.013C262.799 512.113 262.862 512.248 262.862 512.389V518.316L267.78 523.497C267.814 523.616 267.814 523.741 267.78 523.859V527.718L272.411 529.978C272.482 
 530.01 272.544 530.055 272.593 530.11C272.643 530.165 272.678 530.229 272.697 530.298C272.757 530.428 272.757 530.573 272.697 530.703L271.575 532.536V536.928L275.061 539.785C275.162 539.856 
 275.233 539.958 275.259 540.071C275.285 540.184 275.266 540.302 275.204 540.403L274.058 542.535V545.605L277.09 549.635H279.286C279.406 549.633 279.524 549.665 279.622 549.726C279.721 549.787 
 279.795 549.875 279.835 549.976L284.037 560.188C284.048 560.251 284.048 560.316 284.037 560.38V562.085H286.018C286.177 562.085 286.328 562.141 286.44 562.241C286.552 562.341 286.615 562.477 
 286.615 562.618V564.75L288.239 567.116L296.833 560.145L296.021 559.25C295.988 559.174 295.973 559.094 295.977 559.013C295.981 558.932 296.004 558.853 296.045 558.781Z" 
 fill="#ef4444" stroke="black"></path>
 
 <!-- Qunfudah -->
<path id="Vector_qunfudah" d="M
 288.25 566.03 L297.42,559.48 L296.11, 558.17 L297.42, 551.62 L293.49, 541.14 L283.01, 541.14 L280.39, 538.52 L280.39, 524.10 L280.39, 516.24 L271.22, 516.24 L263.36, 509.69 L262.05, 491.35 L256.81, 491.35
 L256.81, 487.42 L245.01, 492.66 L250.25, 500.52 L255.49, 500.52 L255.49, 507.07 L260.74, 511.00 L262.05, 511.00 L262.05, 517.55 L267.29, 522.79 L267.29, 526.72 L272.53, 529.34 L271.22, 530.65 L271.22, 535.90
 L275.15, 538.52 L273.84, 541.14 L273.84, 545.07 L276.46, 549.00 L279.08, 549.00 L282.32, 562.48 L283.01, 562.79 L286.94, 560.79 L286.94, 564.72 288.25 566.03Z
 " 
 fill="#eab308" stroke="black"></path>
 
 <!-- Khulis -->
<path id="Vector_khulis" d="M
 217.50, 378.66 L205.71, 386.53 L203.08, 382.60 L199.15, 383.91 L196.53, 389.15 L191.29, 393.08 L193.91, 400.63 L191.91, 402.63 L209.64, 405.42 L210.95, 404.25 L217.50, 403.56 L221.43, 404.87 L225.36, 403.56
 L224.05, 402.25 L220.74, 398.32 L222.74, 395.70 L220.12, 394.39 L210.95, 394.39 L209.64, 395.70 L209.64, 390.46 L220.12, 379.97 217.50, 378.66Z
 " 
 fill="#16a34a" stroke="black"></path>
 
 <!-- Kamel -->
<path id="Vector_kamel" d="M
 227.98, 390.77 L222.74, 395.88 L220.12, 394.39 L210.95, 394.08 L209.64, 394.39 L209.64, 389.15 L220.12, 379.97 L225.36, 381.28 L225.36, 390.46 227.98, 390.77Z
 " 
 fill="#86efac" stroke="black"></path>
 </g>
 <g id="south" class="group transition ">
 <g id="Group 4964"><path id="Vector_8" d="M
 384.111 488.105L386.499 478.298C386.476 478.229 386.476 478.155 386.499 478.085L390.891 472.883V469.43L387.024 467.063C386.938 467.021 386.87 466.953 386.833 466.871L382.608 459.345L374.252 452.95L363.223 459.111C363.137 459.158 363.038 459.183 362.936 459.183C362.835 459.183 362.736 459.158 362.65 459.111L359.976 457.896H354.199L345.319 459.687L340.138 463.95L339.923 464.057L334.695 465.549L318.868 478.874C318.745 478.96 318.593 479.005 318.438 479.002H314.38C314.272 479.002 314.167 478.977 314.074 478.928C313.982 478.879 313.906 478.809 313.854 478.725L307.122 466.914L305.404 474.653L308.077 476.529C308.147 476.581 308.203 476.646 308.24 476.72C308.277 476.794 308.295 476.874 308.292 476.955V480.025C308.29 480.108 308.268 480.189 308.227 480.263C308.185 480.336 308.126 480.401 308.053 480.452L299.053 486.123V490.877C299.067 490.947 299.067 491.02 299.053 491.09L295.305 499.362L300.796 500.428C300.872 500.44 300.944 500.467 301.006 500.508C301.068 500.549 301.119 500.601 301.154 500.663C301.183 500.723 301.198 500.788 301.198 500.854C301.198 500.92 301.183 500.986 301.154 501.046L299.197 509.041L303.159 515.799C303.221 515.936 303.221 516.089 303.159 516.226L300.701 523.304C300.66 523.41 300.583 523.503 300.48 523.568C300.377 523.633 300.254 523.668 300.128 523.666H290.937L284.73 527.205C284.63 527.262 284.514 527.292 284.396 527.292C284.277 527.292 284.161 527.262 284.061 527.205L281.388 525.564V539.208L283.441 541.084H293.825C293.945 541.086 294.061 541.119 294.158 541.18C294.256 541.24 294.331 541.326 294.374 541.425L299.268 552.085C299.304 552.196 299.304 552.315 299.268 552.426L297.287 558.822L298.075 559.717H303.422C303.509 559.718 303.594 559.736 303.673 559.769C303.751 559.802 303.82 559.85 303.876 559.909C303.934 559.962 303.977 560.026 304.002 560.096C304.026 560.167 304.032 560.241 304.019 560.314L302.419 570.974H309.868C309.981 570.975 310.091 571.006 310.184 571.063C310.278 571.12 310.35 571.2 310.393 571.294L312.78 576.069H322.711C322.816 576.067 322.92 576.089 323.012 576.134C323.104 576.179 323.182 576.245 323.236 576.325L329.515 585.962H335.125V579.822C335.123 579.762 335.134 579.703 335.159 579.648C335.183 579.593 335.221 579.543 335.268 579.502L341.069 572.914C341.121 572.85 341.189 572.797 341.268 572.76C341.347 572.723 341.434 572.703 341.523 572.701H345.271C345.429 572.701 345.581 572.757 345.693 572.857C345.805 572.957 345.868 573.093 345.868 573.234V578.734L349.807 580.312C349.952 580.379 350.063 580.494 350.117 580.632L352.695 587.028H356.706C356.79 587.025 356.873 587.041 356.948 587.075C357.023 587.108 357.088 587.158 357.135 587.219L359.69 589.735H365.061C365.202 589.732 365.339 589.778 365.443 589.863L373.297 596.152L374.228 594.617V588.968L373.011 587.561C372.957 587.502 372.918 587.433 372.897 587.359C372.877 587.286 372.875 587.209 372.891 587.134L374.539 578.969L373.058 564.877C373.055 564.731 373.105 564.589 373.202 564.472L392.801 543.152C392.857 543.093 392.926 543.045 393.004 543.012C393.083 542.978 393.168 542.961 393.255 542.96H397.743L404.594 538.398L403.544 523.091C403.531 522.987 403.554 522.883 403.61 522.792C403.665 522.7 403.75 522.626 403.854 522.579L409.918 519.765V512.516L384.255 488.66C384.172 488.59 384.114 488.501 384.089 488.402C384.063 488.303 384.071 488.2 384.111 488.105Z" 
 fill="currentColor" stroke="black"></path>
 <path id="Vector_9" d="M
 428.992 523.306C428.891 523.337 428.782 523.337 428.681 523.306L409 512.5L407.5 519C407.495 519.098 408 517.5 411.038 520.426C409 518.877 408.097 519.455 408 519.5L403 523.306L401.5 538.824C401.508 538.911 399.542 536.921 399.5 537C399.458 537.079 401.581 538.775 401.5 538.824L397.957 541C397.861 541.066 397.121 542.997 397 543L392 541L369.5 569L374.228 577.5L372 578.95V588.778V591C372.034 591.104 373.534 588.674 373.5 588.778V594.918C370.15 594 372.021 594.834 372 594.918L374.228 597.05L375.756 598.265H379.599C379.716 598.235 379.84 598.235 379.957 598.265L384.302 601.165H385.997L389.53 596.901C389.575 596.843 389.633 596.794 389.7 596.757C389.766 596.719 389.84 596.693 389.918 596.681C389.996 596.67 390.075 596.672 390.152 596.687C390.229 596.703 390.302 596.732 390.366 596.773L393.111 598.585L398.506 596.453H398.745H439.71C439.796 596.431 439.887 596.431 439.973 596.453L447.135 599.758L486.763 604.022L503.092 602.401C503.203 602.389 503.315 602.404 503.416 602.446C503.517 602.487 503.604 602.553 503.665 602.636L513.453 615.598H518.92L529.519 609.884L533.005 585.452L543.007 512.774L469.742 521.707L428.992 523.306Z" 
 fill="currentColor" stroke="black"></path>

 
 <path id="Vector_10" d="M289.505 468.961H284.396C284.277 468.96 284.161 468.927 284.063 468.866C283.965 468.805 283.89 468.719 283.847 468.62L280.577 461.755H277.569L276.017 463.29V471.456C276.03 471.526 276.03 471.598 276.017 471.669L270.526 483.544C270.48 483.639 270.403 483.72 270.305 483.777C270.208 483.834 270.094 483.864 269.977 483.863H262.386L257.611 487.936V491.922H262.076C262.151 491.919 262.226 491.93 262.297 491.953C262.367 491.976 262.432 492.011 262.488 492.057C262.543 492.102 262.588 492.157 262.62 492.218C262.651 492.279 262.669 492.345 262.672 492.413L264.105 509.767L271.481 516.781H280.338V510.385C280.314 510.308 280.314 510.227 280.338 510.15L285.9 500.77C285.952 500.686 286.028 500.616 286.12 500.567C286.213 500.518 286.318 500.492 286.426 500.493H293.587L298 498.5L299 492.5L300.5 490.5C300.502 490.414 300.455 489.837 299.5 486.5C302.455 486.837 304.28 487.991 304.354 487.936L307.5 482L313 487.936L310.5 481C316.646 485.456 310.538 479.818 310.5 479.728C310.462 479.637 308.978 475.366 309 475.272L307 466L302.444 466.616L289.505 468.961Z" 
 fill="currentColor" stroke="black"></path>
 
 <path id="Vector_11" d="M289.028 568.075L294.638 576.241L319.132 595.642C319.253 595.749 319.321 595.894 319.323 596.047V599.692H319.657C319.815 599.692 319.967 599.748 320.079 599.848C320.191 599.948 320.254 600.084 320.254 600.225V606.621H322.163C322.28 606.621 322.394 606.651 322.492 606.708C322.589 606.764 322.666 606.846 322.713 606.941L325.506 612.463H327.702C327.847 612.466 327.986 612.515 328.095 612.601C328.204 612.686 328.276 612.803 328.299 612.932L329.421 619.626L334.911 623.89L335.031 624.018L337.275 627.365C337.309 627.455 337.309 627.552 337.275 627.642V633.015L339.376 635.146C339.466 635.225 339.517 635.332 339.519 635.445L339.949 638.941H343.291L344.938 637.918V634.848C344.935 634.738 344.97 634.63 345.038 634.538C345.106 634.446 345.205 634.376 345.32 634.336L351.646 632.204V627.535C351.646 627.394 351.709 627.259 351.821 627.159C351.933 627.059 352.085 627.002 352.243 627.002H356.898L358.02 622.845L352.076 617.92C351.975 617.825 351.919 617.699 351.919 617.569C351.919 617.438 351.975 617.312 352.076 617.217L356.134 612.249L353.747 610.757C353.669 610.705 353.607 610.637 353.566 610.559C353.524 610.481 353.504 610.396 353.508 610.309V607.794C353.499 607.716 353.499 607.637 353.508 607.559L356.468 602.336C356.514 602.246 356.588 602.17 356.682 602.117C356.775 602.064 356.883 602.037 356.994 602.037H359.524V600.055H357.137C356.979 600.055 356.827 599.999 356.715 599.899C356.603 599.799 356.54 599.663 356.54 599.522V593.126C356.547 593.012 356.588 592.901 356.659 592.806L358.521 590.418L356.301 588.286H352.124C352 588.289 351.879 588.258 351.776 588.197C351.674 588.136 351.595 588.048 351.551 587.945L349.187 581.294L345.153 579.652C345.046 579.61 344.955 579.542 344.892 579.455C344.828 579.367 344.794 579.266 344.795 579.162V573.832H341.954L336.439 580.078V586.474C336.439 586.616 336.376 586.751 336.264 586.851C336.153 586.951 336.001 587.007 335.842 587.007H329.278C329.174 587.006 329.072 586.979 328.984 586.931C328.896 586.882 328.824 586.812 328.776 586.73L322.498 577.115H312.519C312.402 577.115 312.288 577.085 312.191 577.028C312.093 576.972 312.016 576.89 311.97 576.795L309.583 572.02H301.824C301.654 572.019 301.49 571.957 301.37 571.849C301.267 571.727 301.216 571.576 301.227 571.423L302.851 560.763H298.076L290.771 566.69L289.028 568.075Z" 
 fill="currentColor" stroke="black"></path></g></g></svg>
 </div>
 
 {info_cards}
 
 {color_dist}
 
 <p class="text-black absolute p-3 font-bold" id="coordinates" style="top:0px;left:0px"></p>
</div>


<script src="https://kit.fontawesome.com/098817b304.js" crossorigin="anonymous"></script>
{scripting}

"""

# Embedding the map in the Streamlit app
components.html(map_html, height=2000)
