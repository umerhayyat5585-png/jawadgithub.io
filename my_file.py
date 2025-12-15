<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Jawad Balouch - SEO Expert | On-Page, Off-Page & Technical SEO Specialist</title>
    <meta name="description" content="Professional SEO services: On-page SEO, Off-page SEO, Technical SEO. Contact Jawad Balouch for website optimization and search engine ranking improvement.">
    <meta name="keywords" content="SEO expert, on-page SEO, off-page SEO, technical SEO, search engine optimization, SEO services">
    <meta name="author" content="Jawad Balouch">
    
    <!-- Open Graph / Social Media Meta Tags -->
    <meta property="og:title" content="Jawad Balouch - SEO Expert">
    <meta property="og:description" content="Professional SEO services: On-page, Off-page & Technical SEO">
    <meta property="og:type" content="website">
    
    <!-- Font Awesome for icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    
    <!-- Google Fonts -->
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&family=Roboto:wght@300;400;500&display=swap" rel="stylesheet">
    
    <style>
        :root {
            --primary-color: #2c3e50;
            --secondary-color: #3498db;
            --accent-color: #e74c3c;
            --light-color: #ecf0f1;
            --dark-color: #2c3e50;
            --gray-color: #95a5a6;
            --success-color: #27ae60;
            --shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
            --transition: all 0.3s ease;
        }
        
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        html {
            scroll-behavior: smooth;
        }
        
        body {
            font-family: 'Roboto', sans-serif;
            line-height: 1.6;
            color: #333;
            background-color: #f9f9f9;
        }
        
        h1, h2, h3, h4, h5 {
            font-family: 'Poppins', sans-serif;
            font-weight: 600;
            margin-bottom: 1rem;
            color: var(--primary-color);
        }
        
        h1 {
            font-size: 2.8rem;
            line-height: 1.2;
        }
        
        h2 {
            font-size: 2.2rem;
            text-align: center;
            margin-bottom: 2.5rem;
            position: relative;
        }
        
        h2:after {
            content: '';
            position: absolute;
            bottom: -10px;
            left: 50%;
            transform: translateX(-50%);
            width: 80px;
            height: 4px;
            background-color: var(--secondary-color);
        }
        
        p {
            margin-bottom: 1rem;
            font-size: 1.05rem;
        }
        
        .container {
            width: 90%;
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 15px;
        }
        
        section {
            padding: 80px 0;
        }
        
        .btn {
            display: inline-block;
            background-color: var(--secondary-color);
            color: white;
            padding: 12px 28px;
            border-radius: 4px;
            text-decoration: none;
            font-weight: 500;
            transition: var(--transition);
            border: none;
            cursor: pointer;
            font-family: 'Poppins', sans-serif;
        }
        
        .btn:hover {
            background-color: #2980b9;
            transform: translateY(-3px);
            box-shadow: var(--shadow);
        }
        
        /* Header & Navigation */
        header {
            background-color: white;
            box-shadow: var(--shadow);
            position: fixed;
            width: 100%;
            top: 0;
            z-index: 1000;
        }
        
        nav {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 20px 0;
        }
        
        .logo {
            font-family: 'Poppins', sans-serif;
            font-size: 1.8rem;
            font-weight: 700;
            color: var(--primary-color);
            text-decoration: none;
        }
        
        .logo span {
            color: var(--secondary-color);
        }
        
        .nav-links {
            display: flex;
            list-style: none;
        }
        
        .nav-links li {
            margin-left: 30px;
        }
        
        .nav-links a {
            text-decoration: none;
            color: var(--primary-color);
            font-weight: 500;
            transition: var(--transition);
        }
        
        .nav-links a:hover {
            color: var(--secondary-color);
        }
        
        .menu-toggle {
            display: none;
            font-size: 1.5rem;
            cursor: pointer;
            color: var(--primary-color);
        }
        
        /* Hero Section */
        .hero {
            background: linear-gradient(135deg, var(--primary-color) 0%, #1a2530 100%);
            color: white;
            padding: 150px 0 100px;
            margin-top: 70px;
            text-align: center;
        }
        
        .hero h1 {
            color: white;
            margin-bottom: 20px;
        }
        
        .hero p {
            font-size: 1.2rem;
            max-width: 700px;
            margin: 0 auto 30px;
            opacity: 0.9;
        }
        
        .hero-btns {
            margin-top: 30px;
        }
        
        .hero-btns .btn {
            margin: 0 10px;
        }
        
        .btn-outline {
            background-color: transparent;
            border: 2px solid white;
        }
        
        .btn-outline:hover {
            background-color: white;
            color: var(--primary-color);
        }
        
        /* About Section */
        .about-content {
            display: flex;
            align-items: center;
            gap: 50px;
        }
        
        .about-text {
            flex: 1;
        }
        
        .about-image {
            flex: 1;
            text-align: center;
        }
        
        .about-image img {
            max-width: 100%;
            border-radius: 10px;
            box-shadow: var(--shadow);
        }
        
        /* Services Section */
        .services {
            background-color: #f1f8ff;
        }
        
        .services-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 30px;
            margin-top: 40px;
        }
        
        .service-card {
            background-color: white;
            padding: 30px;
            border-radius: 8px;
            box-shadow: var(--shadow);
            transition: var(--transition);
            text-align: center;
        }
        
        .service-card:hover {
            transform: translateY(-10px);
        }
        
        .service-icon {
            font-size: 3rem;
            color: var(--secondary-color);
            margin-bottom: 20px;
        }
        
        .service-card h3 {
            font-size: 1.5rem;
            margin-bottom: 15px;
        }
        
        /* Skills Section */
        .skills-container {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 30px;
        }
        
        .skill-item {
            background-color: white;
            padding: 25px;
            border-radius: 8px;
            box-shadow: var(--shadow);
        }
        
        .skill-header {
            display: flex;
            align-items: center;
            margin-bottom: 15px;
        }
        
        .skill-icon {
            font-size: 2rem;
            color: var(--secondary-color);
            margin-right: 15px;
        }
        
        .skill-details ul {
            list-style-position: inside;
            margin-left: 10px;
        }
        
        .skill-details li {
            margin-bottom: 8px;
            padding-left: 5px;
        }
        
        /* Contact Section */
        .contact {
            background-color: var(--primary-color);
            color: white;
        }
        
        .contact h2 {
            color: white;
        }
        
        .contact h2:after {
            background-color: var(--accent-color);
        }
        
        .contact-container {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 40px;
        }
        
        .contact-info {
            display: flex;
            flex-direction: column;
            justify-content: center;
        }
        
        .contact-item {
            display: flex;
            align-items: center;
            margin-bottom: 25px;
        }
        
        .contact-icon {
            font-size: 1.5rem;
            color: var(--secondary-color);
            margin-right: 15px;
            width: 40px;
        }
        
        .contact-form {
            background-color: white;
            color: #333;
            padding: 30px;
            border-radius: 8px;
            box-shadow: var(--shadow);
        }
        
        .form-group {
            margin-bottom: 20px;
        }
        
        .form-group label {
            display: block;
            margin-bottom: 8px;
            font-weight: 500;
        }
        
        .form-group input,
        .form-group textarea {
            width: 100%;
            padding: 12px 15px;
            border: 1px solid #ddd;
            border-radius: 4px;
            font-family: 'Roboto', sans-serif;
            font-size: 1rem;
        }
        
        .form-group textarea {
            min-height: 150px;
            resize: vertical;
        }
        
        /* Footer */
        footer {
            background-color: #1a2530;
            color: white;
            padding: 40px 0 20px;
            text-align: center;
        }
        
        .footer-content {
            display: flex;
            flex-direction: column;
            align-items: center;
            margin-bottom: 30px;
        }
        
        .social-links {
            display: flex;
            margin: 20px 0;
        }
        
        .social-links a {
            display: flex;
            align-items: center;
            justify-content: center;
            width: 40px;
            height: 40px;
            background-color: rgba(255, 255, 255, 0.1);
            border-radius: 50%;
            margin: 0 10px;
            color: white;
            text-decoration: none;
            transition: var(--transition);
        }
        
        .social-links a:hover {
            background-color: var(--secondary-color);
            transform: translateY(-5px);
        }
        
        .copyright {
            border-top: 1px solid rgba(255, 255, 255, 0.1);
            padding-top: 20px;
            font-size: 0.9rem;
            color: rgba(255, 255, 255, 0.7);
        }
        
        /* Responsive Styles */
        @media (max-width: 992px) {
            h1 {
                font-size: 2.4rem;
            }
            
            h2 {
                font-size: 2rem;
            }
            
            .about-content {
                flex-direction: column;
            }
            
            .about-text, .about-image {
                flex: none;
                width: 100%;
            }
        }
        
        @media (max-width: 768px) {
            .menu-toggle {
                display: block;
            }
            
            .nav-links {
                position: fixed;
                top: 70px;
                left: 0;
                width: 100%;
                background-color: white;
                flex-direction: column;
                align-items: center;
                padding: 20px 0;
                box-shadow: var(--shadow);
                transform: translateY(-100%);
                opacity: 0;
                visibility: hidden;
                transition: var(--transition);
            }
            
            .nav-links.active {
                transform: translateY(0);
                opacity: 1;
                visibility: visible;
            }
            
            .nav-links li {
                margin: 15px 0;
            }
            
            section {
                padding: 60px 0;
            }
        }
        
        @media (max-width: 576px) {
            h1 {
                font-size: 2rem;
            }
            
            h2 {
                font-size: 1.8rem;
            }
            
            .hero {
                padding: 120px 0 80px;
            }
            
            .hero-btns .btn {
                display: block;
                margin: 10px auto;
                width: 80%;
                max-width: 250px;
            }
        }
    </style>
</head>
<body>
    <!-- Header & Navigation -->
    <header>
        <div class="container">
            <nav>
                <a href="#home" class="logo">Jawad<span>SEO</span></a>
                
                <div class="menu-toggle" id="menuToggle">
                    <i class="fas fa-bars"></i>
                </div>
                
                <ul class="nav-links" id="navLinks">
                    <li><a href="#home">Home</a></li>
                    <li><a href="#about">About</a></li>
                    <li><a href="#services">Services</a></li>
                    <li><a href="#skills">Skills</a></li>
                    <li><a href="#contact">Contact</a></li>
                </ul>
            </nav>
        </div>
    </header>

    <!-- Hero Section -->
    <section class="hero" id="home">
        <div class="container">
            <h1>Jawad Balouch - SEO Expert</h1>
            <p>Professional SEO specialist providing comprehensive on-page, off-page, and technical SEO services to boost your website's visibility and drive organic traffic.</p>
            <div class="hero-btns">
                <a href="#contact" class="btn">Get In Touch</a>
                <a href="#services" class="btn btn-outline">My Services</a>
            </div>
        </div>
    </section>

    <!-- About Section -->
    <section class="about" id="about">
        <div class="container">
            <h2>About Me</h2>
            <div class="about-content">
                <div class="about-text">
                    <p>I am Jawad Balouch, a dedicated SEO expert with extensive experience in improving website rankings and driving organic traffic. My expertise spans across all aspects of search engine optimization.</p>
                    <p>With a data-driven approach and staying updated with the latest SEO trends and algorithm changes, I help businesses of all sizes achieve their digital marketing goals through effective SEO strategies.</p>
                    <p>My methodology involves thorough analysis, strategic planning, and continuous optimization to ensure sustainable growth in search engine rankings.</p>
                    <a href="#contact" class="btn" style="margin-top: 20px;">Work With Me</a>
                </div>
                <div class="about-image">
                    <!-- Placeholder for profile image -->
                    <div style="width: 100%; height: 400px; background-color: #e0e0e0; border-radius: 10px; display: flex; align-items: center; justify-content: center; color: #777; font-size: 1.2rem;">
                        <div>Profile Image</div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Services Section -->
    <section class="services" id="services">
        <div class="container">
            <h2>My SEO Services</h2>
            <div class="services-grid">
                <div class="service-card">
                    <div class="service-icon">
                        <i class="fas fa-search-plus"></i>
                    </div>
                    <h3>On-Page SEO</h3>
                    <p>Optimizing individual web pages to rank higher and earn more relevant traffic. This includes content optimization, meta tags, heading structure, URL optimization, and internal linking.</p>
                </div>
                
                <div class="service-card">
                    <div class="service-icon">
                        <i class="fas fa-external-link-alt"></i>
                    </div>
                    <h3>Off-Page SEO</h3>
                    <p>Building your website's reputation and authority through backlinks, social signals, and brand mentions. This includes link building, influencer outreach, and social media marketing.</p>
                </div>
                
                <div class="service-card">
                    <div class="service-icon">
                        <i class="fas fa-cogs"></i>
                    </div>
                    <h3>Technical SEO</h3>
                    <p>Improving the technical aspects of your website for better crawling and indexing. This includes site speed optimization, mobile-friendliness, site architecture, and fixing crawl errors.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Skills Section -->
    <section class="skills" id="skills">
        <div class="container">
            <h2>SEO Skills & Expertise</h2>
            <div class="skills-container">
                <div class="skill-item">
                    <div class="skill-header">
                        <div class="skill-icon">
                            <i class="fas fa-chart-line"></i>
                        </div>
                        <h3>On-Page SEO Details</h3>
                    </div>
                    <div class="skill-details">
                        <ul>
                            <li>Keyword Research & Analysis</li>
                            <li>Content Optimization & Strategy</li>
                            <li>Title Tag & Meta Description Optimization</li>
                            <li>Header Tag Optimization (H1, H2, H3)</li>
                            <li>URL Structure Optimization</li>
                            <li>Image Optimization with Alt Text</li>
                            <li>Internal Linking Strategy</li>
                            <li>Schema Markup Implementation</li>
                        </ul>
                    </div>
                </div>
                
                <div class="skill-item">
                    <div class="skill-header">
                        <div class="skill-icon">
                            <i class="fas fa-link"></i>
                        </div>
                        <h3>Off-Page SEO Details</h3>
                    </div>
                    <div class="skill-details">
                        <ul>
                            <li>High-Quality Backlink Building</li>
                            <li>Guest Posting & Outreach</li>
                            <li>Social Media Marketing</li>
                            <li>Influencer Collaboration</li>
                            <li>Brand Mention Monitoring</li>
                            <li>Local SEO & Citation Building</li>
                            <li>Online Reputation Management</li>
                            <li>Directory Submissions</li>
                        </ul>
                    </div>
                </div>
                
                <div class="skill-item">
                    <div class="skill-header">
                        <div class="skill-icon">
                            <i class="fas fa-tools"></i>
                        </div>
                        <h3>Technical SEO Details</h3>
                    </div>
                    <div class="skill-details">
                        <ul>
                            <li>Website Speed Optimization</li>
                            <li>Mobile-Friendly Optimization</li>
                            <li>XML Sitemap Creation</li>
                            <li>Robots.txt Optimization</li>
                            <li>Structured Data Implementation</li>
                            <li>Canonical URL Management</li>
                            <li>404 Error Monitoring & Fixing</li>
                            <li>Website Migration SEO</li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Contact Section -->
    <section class="contact" id="contact">
        <div class="container">
            <h2>Contact Me</h2>
            <div class="contact-container">
                <div class="contact-info">
                    <p>Ready to improve your website's search engine rankings? Get in touch for a free consultation and SEO audit.</p>
                    
                    <div class="contact-item">
                        <div class="contact-icon">
                            <i class="fas fa-phone-alt"></i>
                        </div>
                        <div>
                            <h3>Phone Number</h3>
                            <p>0313-6633572</p>
                        </div>
                    </div>
                    
                    <div class="contact-item">
                        <div class="contact-icon">
                            <i class="fas fa-envelope"></i>
                        </div>
                        <div>
                            <h3>Business Email</h3>
                            <p>balouchjawad0@gmail.com</p>
                        </div>
                    </div>
                    
                    <div class="contact-item">
                        <div class="contact-icon">
                            <i class="fas fa-map-marker-alt"></i>
                        </div>
                        <div>
                            <h3>Location</h3>
                            <p>Available for remote work worldwide</p>
                        </div>
                    </div>
                </div>
                
                <div class="contact-form">
                    <h3 style="color: var(--primary-color);">Send a Message</h3>
                    <form id="contactForm">
                        <div class="form-group">
                            <label for="name">Full Name</label>
                            <input type="text" id="name" required>
                        </div>
                        
                        <div class="form-group">
                            <label for="email">Email Address</label>
                            <input type="email" id="email" required>
                        </div>
                        
                        <div class="form-group">
                            <label for="subject">Subject</label>
                            <input type="text" id="subject" required>
                        </div>
                        
                        <div class="form-group">
                            <label for="message">Message</label>
                            <textarea id="message" required></textarea>
                        </div>
                        
                        <button type="submit" class="btn">Send Message</button>
                    </form>
                </div>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer>
        <div class="container">
            <div class="footer-content">
                <a href="#home" class="logo" style="color: white; margin-bottom: 20px;">Jawad<span style="color: var(--secondary-color);">SEO</span></a>
                <p>Professional SEO Expert - Driving Organic Growth Through Search Engine Optimization</p>
                
                <div class="social-links">
                    <a href="#"><i class="fab fa-linkedin-in"></i></a>
                    <a href="#"><i class="fab fa-twitter"></i></a>
                    <a href="#"><i class="fab fa-facebook-f"></i></a>
                    <a href="#"><i class="fab fa-instagram"></i></a>
                </div>
            </div>
            
            <div class="copyright">
                <p>&copy; 2023 Jawad Balouch - SEO Expert. All Rights Reserved.</p>
            </div>
        </div>
    </footer>

    <script>
        // Mobile Menu Toggle
        const menuToggle = document.getElementById('menuToggle');
        const navLinks = document.getElementById('navLinks');
        
        menuToggle.addEventListener('click', () => {
            navLinks.classList.toggle('active');
        });
        
        // Close mobile menu when clicking on a link
        document.querySelectorAll('.nav-links a').forEach(link => {
            link.addEventListener('click', () => {
                navLinks.classList.remove('active');
            });
        });
        
        // Form submission handling
        const contactForm = document.getElementById('contactForm');
        
        contactForm.addEventListener('submit', (e) => {
            e.preventDefault();
            
            // Get form values
            const name = document.getElementById('name').value;
            const email = document.getElementById('email').value;
            const subject = document.getElementById('subject').value;
            const message = document.getElementById('message').value;
            
            // In a real implementation, you would send this data to a server
            // For this example, we'll just show an alert
            alert(`Thank you ${name}! Your message has been received. I will contact you at ${email} soon.`);
            
            // Reset the form
            contactForm.reset();
        });
        
        // Smooth scrolling for navigation links
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function(e) {
                e.preventDefault();
                
                const targetId = this.getAttribute('href');
                if(targetId === '#') return;
                
                const targetElement = document.querySelector(targetId);
                if(targetElement) {
                    window.scrollTo({
                        top: targetElement.offsetTop - 70,
                        behavior: 'smooth'
                    });
                }
            });
        });
    </script>
</body>
</html>
