__ACCOUNTING = "accounting"
__HUMAN_RESOURCE = "human resource"
__ARTS_MEDIA = "arts media"
__EDUCATION = "education"
__TECHNOLOGY = "technology"
__ENGINEERING = "engineering"
__HEALTH = "health"
__SERVICES = "services"


JOB_FIELDS = [
    __ACCOUNTING,
    __HUMAN_RESOURCE,
    __ARTS_MEDIA,
    __EDUCATION,
    __TECHNOLOGY,
    __ENGINEERING,
    __HEALTH,
    __SERVICES
]

ROLE_BASELINES = [
    "Senior",
    "Advanced",
    "Head",
    "Expert",
    "Professional",
    "Master"
]

HARD_SKILLS_BASELINES = {
    __ACCOUNTING: [
        "Advanced Financial Analysis",
        "Excel Modeling Mastery",
        "Strategic Database Planning",
        "Oracle & Hyperion Proficiency",
        "Revenue Recognition Expert",
        "ERP Systems Excellence",
        "Audit Process Mastery",
        "Global Compliance Pro",
        "Process Optimization Specialist",
        "Financial Reporting Precision"
    ],
    __HUMAN_RESOURCE: [
        "Strategic Recruitment Management",
        "End-to-End Recruitment Expertise",
        "Advanced Analytical Reporting",
        "Compliance Oversight",
        "Document Organization Mastery",
        "Digital Tools Proficiency",
        "Vendor Relationship Leadership",
        "Recruitment Strategy Development",
        "Streamlined Document Retrieval Systems",
        "Up-to-Date HR Technology Knowledge"
    ],
    __ARTS_MEDIA: [
        "Advanced Multimedia Production",
        "Expert Video Editing and Production",
        "Strategic Digital Marketing",
        "Mastery of Design Tools (Adobe Creative Suite)",
        "Proficient in Google Ads Management",
        "In-depth Research for Animations and Special Effects",
        "High-level Social Media Management",
        "Proven Event Planning and Management",
        "Advanced Website Management and Optimization",
        "Professional Copywriting for Marketing Communications"
    ],
    __EDUCATION: [
        "Curriculum Development and Implementation",
        "Formative and Summative Assessment Expertise",
        "Student Progress Tracking and Analysis",
        "Classroom Management and Adaptability",
        "Educational Technology Integration",
        "Admission Process Management and Evaluation",
        "Scholarship Administration and Management",
        "Student Counseling and Guidance Services",
        "Examination Proctoring and Administration",
        "Substitute Teaching and Continuity Maintenance"
    ],
    __TECHNOLOGY: [
        "IT Troubleshooting",
        "Network Access Control",
        "Backup Systems Management",
        "Third-Party Software Negotiation",
        "Host Performance Monitoring",
        "System Implementation Planning",
        "Security and Privacy Audits",
        "Network Security Implementation",
        "Cloud Technical Implementations",
        "IaaS Infrastructure Implementation"
    ],
    __ENGINEERING: [
        "Advanced statistical methods and mathematical modeling",
        "Quality control and reliability optimization",
        "Proficient in drafting and design using advanced tools",
        "Production schedule analysis and optimization",
        "Formulating and implementing sampling procedures",
        "Strong record-keeping and documentation skills",
        "In-depth knowledge of operations sequences and material flow",
        "Expert in product measurement, inspection, and testing",
        "Precision and accuracy evaluation of engineering drawings",
        "Statistical data analysis for product specifications"
    ],
    __HEALTH: [
        "Diagnostic imaging technology proficiency.",
        "Ultrasound scanner programming expertise.",
        "Medical record maintenance knowledge.",
        "Image quality evaluation skills.",
        "Diagnostic test ordering proficiency.",
        "Patient condition monitoring expertise.",
        "Blood sample collection precision.",
        "Ultrasound equipment maintenance.",
        "Strict protocol adherence.",
        "Microsoft Office and Google apps proficiency."
    ],
    __SERVICES: [
        "Strategic Planning",
        "Financial Analysis",
        "Project Management",
        "Data Analysis",
        "Market Research",
        "Technology Integration",
        "Risk Management",
        "Contract Negotiation",
        "Regulatory Compliance",
        "Quality Assurance"
    ]
}

SOFT_SKILLS_BASELINES = {
    __ACCOUNTING: [
        "Elite Communication Skills",
        "Analytical Problem-Solver",
        "Superior Time Management",
        "Ethical Professionalism",
        "Strategic Leadership",
        "Collaborative Communicator",
        "Efficient Multitasker",
        "Unwavering Ethical Conduct",
        "Stress Management Expert",
        "Continuous Improvement Leader"
    ],
    __HUMAN_RESOURCE: [
        "Transformational Leadership",
        "Coaching and Mentorship Excellence",
        "Effective Team Collaboration",
        "Strategic Problem-Solving",
        "Balanced Decision-Making",
        "Exceptional Client Relationship Management",
        "Adaptability and Flexibility",
        "Continuous Learning Commitment",
        "Global Cultural Awareness",
        "Agile Approach to HR Challenges"
    ],
    __ARTS_MEDIA: [
        "Creative Visionary",
        "Strategic Thinker",
        "Effective Communication Strategist",
        "Adaptable Innovator",
        "Team Collaboration Expert",
        "Analytical Problem Solver",
        "Empathetic Brand Ambassador",
        "Masterful Negotiator",
        "Agile Project Manager",
        "Inspirational Leadership"
    ],
    __EDUCATION: [
        "Flexibility and Adaptability in Teaching Approaches",
        "Timely and Constructive Feedback Delivery",
        "Meticulous Record-Keeping and Organization",
        "Open and Effective Communication",
        "Collaborative Teamwork and Contribution",
        "Outstanding Results in High-Pressure Environments",
        "Customer Service and Relationship Building",
        "Attention to Detail in Application Evaluation",
        "Proactive Problem Solving and Decision Making",
        "Continuous Learning and Skill Enhancement"
    ],
    __TECHNOLOGY: [
        "Strong Analytical and Problem-Solving Skills",
        "Effective Communication",
        "Proactive and Adaptable Approach",
        "Exceptional Leadership",
        "Resilience and Adaptability",
        "Collaborative Teamwork",
        "Problem-Solving Expertise",
        "Proactive Approach",
        "Effective Communication Skills",
        "Project Managemen"
    ],
    __ENGINEERING: [
        "Effective communication and collaboration",
        "Strong problem-solving and critical-thinking abilities",
        "Exceptional leadership and teamwork skills",
        "Adaptability and flexibility in dynamic environments",
        "Strategic thinking and decision-making",
        "Continuous learning mindset",
        "Attention to detail and analytical skills",
        "Proactive risk management and problem resolution",
        "Effective planning and organizational skills",
        "Strong accountability and initiative",
    ],
    __HEALTH: [
        "Professionalism and commitment.",
        "Effective communication and empathy.",
        "Accountability for patient care.",
        "Compassion in maternal care.",
        "Collaboration with healthcare teams.",
        "Quick and efficient customer service.",
        "Adherence to attendance and KPIs.",
        "Teleconsultation proficiency.",
        "Health education effectiveness.",
        "Continuous learning mindset."
    ],
    __SERVICES: [
        "Leadership Excellence",
        "Critical Thinking",
        "Decision-making",
        "Emotional Intelligence",
        "Adaptability",
        "Collaboration",
        "Conflict Resolution",
        "Client Relationship Management",
        "Effective Communication",
        "Innovation Leadership"
    ]
}

EXPERIENCE_BASELINES = {
    __ACCOUNTING: [
        "Accomplished leadership in finance, driving organizational success through strategic planning, risk management, and regulatory compliance.",
        "Proven track record in ensuring meticulous adherence to BIR, SEC, and local government regulations, with expertise in timely and accurate filing using EFPS.",
        "Implemented innovative software solutions for streamlined accounting processes, enhancing overall financial efficiency and reporting.",
        "Collaborated seamlessly with department heads, providing valuable financial insights to align business decisions with overarching financial goals.",
        "Demonstrated expertise in end-to-end financial oversight, from precise record-keeping and bank reconciliation to the preparation of insightful financial statements and reports.",
        "Highly motivated and results-oriented professional with a proven track record of success.",
        "Strong analytical and problem-solving skills, with the ability to think creatively and independently.",
        "Excellent communication and interpersonal skills, with the ability to build rapport and work effectively with a diverse team.",
        "Adaptable and flexible, with the ability to learn new skills and concepts quickly.",
        "Committed to excellence and continuous improvement.",
    ],
    __HUMAN_RESOURCE: [
        "Strategic HR leader with a proven track record of driving organizational transformation and talent management excellence.",
        "Highly accomplished HR professional with expertise in developing and implementing comprehensive HR strategies aligned with business objectives.",
        "Seasoned HR executive with a deep understanding of employee relations, compensation and benefits, and performance management.",
        "Visionary HR strategist with a passion for creating a culture of engagement, innovation, and high performance.",
        "Exceptional HR leader with the ability to influence and guide senior management on critical HR issues.",
        "Led transformative initiatives aligning organizational goals with innovative strategies.",
        "Orchestrated global operations, ensuring excellence in service delivery and industry standards adherence.",
        "Excelled in ensuring corporate governance, compliance, and regulatory adherence.",
        "Pioneered data-driven decision-making, leveraging advanced analytics and artificial intelligence.",
        "Defined and implemented groundbreaking human capital strategies aligned with organizational objectives.",
    ],
    __ARTS_MEDIA: [
        "Strategic marketing leader with a proven ability to develop and execute data-driven marketing strategies that drive business growth and brand awareness.",
        "Highly accomplished marketing professional with expertise in creating compelling brand stories and engaging content across multiple channels.",
        "Seasoned marketing executive with a deep understanding of consumer behavior, market trends, and digital marketing platforms.",
        "Creative marketing visionary with a passion for leveraging innovative technologies to deliver exceptional customer experiences.",
        "Exceptional marketing leader with the ability to influence and guide senior management on critical marketing initiatives.",
        "Spearheaded strategic initiatives in multimedia content creation, demonstrating an innovative approach aligned with organizational goals.",
        "Directed the production of high-impact videos and visually compelling artworks, optimizing content strategy for online courses and social media.",
        "Led the design and implementation of digital collaterals, ensuring a consistent and elevated brand presence across diverse platforms.",
        "Drove the conceptualization and execution of marketing campaigns, contributing to increased brand visibility and market penetration.",
        "Orchestrated the development and monitoring of social media and website content, elevating the organization's online presence to new heights.",
    ],
    __EDUCATION: [
        "Successfully led and executed strategic initiatives resulting in measurable business growth and enhanced market positioning.",
        "Demonstrated exceptional leadership skills in guiding cross-functional teams toward achieving ambitious organizational objectives.",
        "Consistently delivered outstanding results, exceeding performance metrics and surpassing expectations in elite-level roles.",
        "Established a track record of effective decision-making in high-pressure situations, showcasing resilience and problem-solving abilities.",
        "Proven ability to drive innovation and optimize operational processes, contributing to increased efficiency and profitability in elite-level positions.",
        "Highly motivated and results-oriented professional with a proven track record of success in education. Passionate about making a difference in students' lives and committed to providing them with the best possible learning experience.",
        "Creative and innovative educator with a strong understanding of child development. Constantly seeking out new and effective ways to teach and engage students. Skilled communicator and able tob uild strong relationships with students, parents, and colleagues.",
        "Dedicated and hardworking professional with a willingness to got the extra mile. Committed to providing students with the support they need to succeed. Team player and always willing to collaborate with colleagues to achieve shared goals.",
        "Highly adaptable and resourceful professional who can thrive in various educational settings. Lifelong learner and always seeking out new opportunities to grow and develop skills.",
        "Passionate and enthusiastic educator committed to making a positive impact on students' lives. Believes in every student's potential and dedicated to helping them reach their full potential."
    ],
    __TECHNOLOGY: [
        "Orchestrated and executed strategic IT initiatives, driving technological innovation and achieving measurable business growth.",
        "Demonstrated exceptional leadership in guiding cross-functional IT teams, ensuring optimal performance and collaboration.",
        "Consistently delivered outstanding results in complex IT projects, exceeding performance metrics and surpassing organizational expectations.",
        "Established a track record of effective decision-making in high-pressure IT environments, showcasing resilience and advanced problem-solving skills.",
        "Proven ability to architect and implement cutting-edge solutions, optimizing operational processes and enhancing overall IT infrastructure efficiency.",
        "Managed technologies and offered administrative assistance for various systems.",
        "Understood and troubleshooted various IT issues, providing technical support.",
        "Controlled and monitored data, network access, and backup systems.",
        "Negotiated and communicated with third-party software providers for new software and troubleshooting.",
        "Developed new system implementation plans, custom scripts, and testing procedures.",
    ],
    __ENGINEERING: [
        "Engineered and designed software solutions to meet clients' needs in marketing and advertising.",
        "Analyzed statistical data and product specifications to determine standards and establish quality and reliability objectives of finished product.",
        "Implemented methods and procedures for disposition of discrepant material and defective or damaged parts and assessed cost and responsibility.",
        "Monitored network health and integrity, and performed on-call duties as a member of the on-call rotation team.",
        "Conducted research and analyzed data to determine feasibility, performance standards, and required equipment.",
        "Accomplished engineering executive with a proven track record in developing and implementing strategic initiatives. Adept at overseeing complex projects, optimizing processes, and driving innovation to achieve organizational objectives.",
        "Seasoned technical director known for delivering exceptional results in engineering operations. Demonstrated ability to lead cross-functional teams, manage large-scale projects, and implement cutting-edge technologies to enhance overall efficiency.",
        "Visionary systems architect with extensive experience in designing and implementing robust engineering solutions. Proficient in leveraging emerging technologies to create scalable and sustainable systems that align with business goals.",
        "Accomplished mechanical engineer with expertise in designing and optimizing mechanical systems. Proven ability to lead engineering teams, manage end-to-end project lifecycles, and deliver solutions that meet and exceed technical specifications.",
        "Dynamic network infrastructure specialist recognized for designing and managing global network architectures. Skilled in establishing technical standards, ensuring network health, and leading teams to deliver high-performance solutions in alignment with business needs.",
    ],
    __HEALTH: [
        "Program and optimize ultrasound scanners for diverse procedures, ensuring precise image capture and presentation of sonograms for diagnostic evaluation by Physicians.",
        "Demonstrate expertise in maintaining, sterilizing, and organizing ultrasound equipment and procedure rooms, adhering to stringent protocols, including those related to handling HIV-related tests and specimens.",
        "Administer medications as prescribed, monitor changes in patient conditions, and order, interpret, and evaluate diagnostic tests to assess and modify patient treatment plans in collaboration with physicians and healthcare team members.",
        "Provide exceptional nursing care, demonstrating accountability for safe and quality patient care, especially in the areas of maternal care, including pregnancy assessment, labor assistance, and support during unexpected situations like miscarriage or stillbirth.",
        "Serve as a first point of contact for customers' healthcare product and service queries, ensuring excellent customer experience, timely issue resolution, and adherence to key performance indicators (KPIs) to maintain high levels of customer satisfaction.",
        "Provide comprehensive ultrasound procedure explanations to patients, answering questions and offering support.",
        "Program and adjust ultrasound scanners for specific procedures, ensuring comprehensive image capture.",
        "Evaluate ultrasound image quality, interpreting images to assist physicians in diagnosing and treating diseases.",
        "Maintain patients' records and medical notes on ultrasound procedures, ensuring patient care continuity.",
        "Maintain and sterilize ultrasound equipment and procedure rooms, upholding hygiene standards.",
    ],
    __SERVICES: [
        "Strategic development and execution of high-impact service solutions.",
        "Proven expertise in optimizing customer experience through service innovations.",
        "Leadership in designing and implementing service excellence frameworks.",
        "Achieving and exceeding KPIs for service quality and customer satisfaction.",
        "Effective management of service delivery operations for seamless execution.",
        "Implementation of cutting-edge technologies to enhance service efficiency.",
        "Proactive problem-solving and resolution in complex service scenarios.",
        "Continuous improvement initiatives for service processes and workflows.",
        "Exceptional interpersonal and communication skills for client engagement.",
        "Strategic analysis and decision-making for service-oriented business growth.",
    ]
}