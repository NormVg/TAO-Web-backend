from tinydb import TinyDB ,Query

db = TinyDB("./db/files/launches.json")
db2 = TinyDB("./db/files/projects.json")
db3 = TinyDB("./db/files/teams.json")





data_launches = [

    {
    "name": "John Smith",
    "one-line-disc": "Experienced professional in various industries.",
    "img": "https://example.com/john_smith.png",
    "disc": {
        "d1": {
            "one-liner": "Masters in Business Administration",
            "disc": "I hold a Master's degree in Business Administration with a focus on strategic management."
        },
        "d2": {
            "one-liner": "Technology Enthusiast",
            "disc": "Passionate about emerging technologies and their impact on businesses."
        },
        "d3": {
            "one-liner": "Problem Solver",
            "disc": "Skilled at finding innovative solutions to complex challenges."
        }
    }
    },
    {
        "name": "Emily Johnson",
        "one-line-disc": "Dedicated to environmental sustainability.",
        "img": "https://example.com/emily_johnson.png",
        "disc": {
            "d1": {
                "one-liner": "Environmental Activist",
                "disc": "Committed to promoting eco-friendly practices and preserving the environment."
            },
            "d2": {
                "one-liner": "Wildlife Conservationist",
                "disc": "Working to protect endangered species and their natural habitats."
            },
            "d3": {
                "one-liner": "Green Energy Advocate",
                "disc": "Promoting the adoption of clean and renewable energy sources."
            }
        }
    },
    {
        "name": "Michael Davis",
        "one-line-disc": "Passionate about art and creativity.",
        "img": "https://example.com/michael_davis.png",
        "disc": {
            "d1": {
                "one-liner": "Visual Artist",
                "disc": "Creating captivating and thought-provoking artwork in various mediums."
            },
            "d2": {
                "one-liner": "Art Education Specialist",
                "disc": "Teaching and inspiring others to explore their artistic talents."
            },
            "d3": {
                "one-liner": "Gallery Curator",
                "disc": "Managing and curating art exhibitions to showcase emerging talents."
            }
        }
    }

]

data_teams = [
    {
        "name": "Alice Smith",
        "disc": "Hello, I'm Alice Smith, known as NormVg. I'm a full-stack developer and the founder of TechPro Innovations.",
        "tags": ["Web Development", "Founder", "UI/UX Design"],
        "contact": {
            "type": "Instagram",
            "url": "https://instagram.com/alicesmith_dev"
        }
    },
    {
        "name": "Samuel Johnson",
        "disc": "Hi, I'm Samuel Johnson, also known as NormVg. I'm a software engineer and the founder of CodeCrafters.",
        "tags": ["Software Development", "Founder", "Coding Enthusiast"],
        "contact": {
            "type": "Twitter",
            "url": "https://twitter.com/sam_j_code"
        }
    },
    {
        "name": "Elena Ramirez",
        "disc": "Greetings! I'm Elena Ramirez, a.k.a. NormVg. I'm a web developer and the co-founder of DesignMasters.",
        "tags": ["Web Design", "Co-Founder", "Creative Professional"],
        "contact": {
            "type": "LinkedIn",
            "url": "https://linkedin.com/in/elena_ramirez"
        }
    }
]

data_projects = [
    {
        "name": "TechWizards Inc.",
        "one-line-disc": "Your digital transformation partner.",
        "disc": "TechWizards Inc. is a leading technology company specializing in digital transformation solutions. We help businesses leverage cutting-edge technology to stay competitive in today's fast-paced market.",
        "status": "Ongoing Projects",
        "team-lead": "Alex Johnson",
        "icon": "https://example.com/techwizards_icon.png",
        "type": "Running",
        "init-date": "2023-03-15",
        "link": [
            {
                "type": "LinkedIn",
                "url": "https://linkedin.com/company/techwizards"
            },
            {
                "type": "GitHub",
                "url": "https://github.com/techwizards"
            },
            {
                "type": "Twitter",
                "url": "https://twitter.com/techwizards"
            }
        ],
        "team": [
            {
                "name": "Emily Davis",
                "contact-url": "https://example.com/emilydavis",
                "pfp": "https://example.com/emilydavis_profile.jpg",
                "role": "Software Engineer"
            },
            {
                "name": "John Smith",
                "contact-url": "https://example.com/johnsmith",
                "pfp": "https://example.com/johnsmith_profile.jpg",
                "role": "UI/UX Designer"
            },
            {
                "name": "Michael Chen",
                "contact-url": "https://example.com/michaelchen",
                "pfp": "https://example.com/michaelchen_profile.jpg",
                "role": "Project Manager"
            }
        ]
    },
    {
        "name": "CreativeMinds Studio",
        "one-line-disc": "Where creativity knows no bounds.",
        "disc": "CreativeMinds Studio is a haven for artists and creators of all kinds. We provide a platform for talented individuals to express themselves and share their art with the world.",
        "status": "Active",
        "team-lead": "Sophia Martinez",
        "icon": "https://example.com/creativeminds_icon.png",
        "type": "Compleated",
        "init-date": "2023-02-20",
        "link": [
            {
                "type": "Instagram",
                "url": "https://instagram.com/creativeminds"
            },
            {
                "type": "DeviantArt",
                "url": "https://deviantart.com/creativeminds"
            },
            {
                "type": "YouTube",
                "url": "https://youtube.com/creativeminds"
            }
        ],
        "team": [
            {
                "name": "Oliver Turner",
                "contact-url": "https://example.com/oliverturner",
                "pfp": "https://example.com/oliverturner_profile.jpg",
                "role": "Digital Artist"
            },
            {
                "name": "Mia Adams",
                "contact-url": "https://example.com/miaadams",
                "pfp": "https://example.com/miaadams_profile.jpg",
                "role": "Animator"
            },
            {
                "name": "Lucas Wilson",
                "contact-url": "https://example.com/lucaswilson",
                "pfp": "https://example.com/lucaswilson_profile.jpg",
                "role": "Music Composer"
            }
        ]
    },
    {
        "name": "EcoSavers Foundation",
        "one-line-disc": "Protecting our planet for future generations.",
        "disc": "EcoSavers Foundation is a non-profit organization dedicated to environmental conservation. We work tirelessly to promote sustainable practices and protect the environment from the threats of climate change and pollution.",
        "status": "Ongoing Campaigns",
        "team-lead": "Sarah Johnson",
        "icon": "https://example.com/ecosavers_icon.png",
        "type": "Running",
        "init-date": "2023-04-10",
        "link": [
            {
                "type": "Website",
                "url": "https://ecosavers.org"
            },
            {
                "type": "Twitter",
                "url": "https://twitter.com/ecosavers"
            },
            {
                "type": "Facebook",
                "url": "https://facebook.com/ecosavers"
            }
        ],
        "team": [
            {
                "name": "Liam Brown",
                "contact-url": "https://example.com/liambrown",
                "pfp": "https://example.com/liambrown_profile.jpg",
                "role": "Environmental Scientist"
            },
            {
                "name": "Sophie Clark",
                "contact-url": "https://example.com/sophieclark",
                "pfp": "https://example.com/sophieclark_profile.jpg",
                "role": "Community Outreach Coordinator"
            },
            {
                "name": "David Miller",
                "contact-url": "https://example.com/davidmiller",
                "pfp": "https://example.com/davidmiller_profile.jpg",
                "role": "Fundraising Specialist"
            }
        ]
    }
]

# db.insert_multiple(data_launches)
# db2.insert_multiple(data_projects)
# db3.insert_multiple(data_teams)