import streamlit as st 


<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Business Landing Page</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>

    <!-- Navigation Bar -->
    <header class="navbar">
        <div class="logo">❤ Business logo</div>

        <nav>
            <a href="#">Home</a>
            <a href="#">New</a>
            <a href="#">Accessories</a>
            <a href="#">Blog</a>
            <a href="#">Contact</a>
        </nav>

        <div class="auth">
            <a href="#">Login</a>
            <a href="#" class="signup">Sign Up</a>
            <span class="cart">🛒</span>
        </div>
    </header>

    <!-- Hero Section -->
    <section class="hero">
        <div class="hero-text">
            <h1>Business<br>Landing Page</h1>
            <p>
                Lorem ipsum dolor sit amet, consectetur adipiscing elit,
                sed diam nonummy. Lorem euismod tincidunt.
            </p>
            <button>Learn More</button>
        </div>

        <div class="hero-image">
            <!-- Replace image URL if needed -->
            <img src="https://cdn-icons-png.flaticon.com/512/1170/1170576.png" alt="Illustration">
        </div>
    </section>

    <!-- Footer -->
    <footer>
        <p>Privacy | User Agreement | Cookies</p>
    </footer>

</body>
</html>

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: Arial, sans-serif;
}

/* Page background */
body {
    background-color: #ff6f91;
}

/* Main container look */
.navbar, .hero, footer {
    background-color: white;
    max-width: 1100px;
    margin: auto;
}

/* Navbar */
.navbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 15px 30px;
    border-radius: 12px 12px 0 0;
}

.logo {
    color: #ff4f7b;
    font-weight: bold;
}

.navbar nav a {
    margin: 0 10px;
    text-decoration: none;
    color: #333;
}

.auth a {
    margin-right: 10px;
    text-decoration: none;
    color: #333;
}

.signup {
    color: #ff4f7b;
}

.cart {
    font-size: 20px;
}

/* Hero section */
.hero {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 40px;
}

.hero-text {
    width: 50%;
}

.hero-text h1 {
    font-size: 2.8rem;
    color: #3d143f;
    margin-bottom: 15px;
}

.hero-text p {
    color: #555;
    margin-bottom: 20px;
}

.hero-text button {
    background-color: #ff4f7b;
    border: none;
    padding: 12px 25px;
    color: white;
    border-radius: 25px;
    cursor: pointer;
}

.hero-image {
    width: 40%;
    text-align: center;
}

.hero-image img {
    width: 100%;
    max-width: 300px;
}

/* Footer */
footer {
    text-align: left;
    padding: 15px 30px;
    color: #888;
    font-size: 0.9rem;
    border-radius: 0 0 12px 12px;
}



