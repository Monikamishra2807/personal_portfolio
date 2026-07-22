from django.core.management.base import BaseCommand
from apps.portfolio.models import Profile, TechCategory, TechStack, SocialLink
from apps.education.models import Education
from apps.experience.models import Experience
from apps.certifications.models import Certification
from apps.projects.models import Project, ProjectTag


class Command(BaseCommand):
    help = 'Seeds the database with portfolio data from Monika Mishra\'s resume'

    def handle(self, *args, **options):
        self.stdout.write('Seeding portfolio data...')

        self._create_profile()
        self._create_social_links()
        self._create_tech_categories()
        self._create_education()
        self._create_experience()
        self._create_projects()
        self._create_certifications()

        self.stdout.write(self.style.SUCCESS('Successfully seeded portfolio data!'))

    def _create_profile(self):
        profile, created = Profile.objects.get_or_create(
            id=1,
            defaults={
                'name': 'Monika Mishra',
                'role': 'Software Developer',
                'tagline': 'Building thoughtful, production-grade software.',
                'biography': 'To obtain a challenging position as a Software Developer where I can leverage my knowledge in programming, web development and problem solving to build efficient software solutions to contribute to dynamic projects and grow as a technology professional.',
                'email': 'monikamis2801@gmail.com',
                'phone': '+91 9092373767',
                'location': 'Tiruppur',
                'is_available': True,
            }
        )
        action = 'Created' if created else 'Updated'
        self.stdout.write(f'  {action} profile: {profile.name}')

    def _create_social_links(self):
        links = [
            {'platform': 'GitHub', 'url': 'https://github.com/Monikamishra', 'icon': 'GH', 'order': 1},
            {'platform': 'LinkedIn', 'url': 'https://linkedin.com/in/monikamishra', 'icon': 'LI', 'order': 2},
        ]
        for link_data in links:
            link, created = SocialLink.objects.get_or_create(
                platform=link_data['platform'],
                defaults=link_data
            )
            action = 'Created' if created else 'Exists'
            self.stdout.write(f'  {action} social link: {link.platform}')

    def _create_tech_categories(self):
        categories = {
            'Languages': ['Java', 'Python', 'C#', 'HTML', 'CSS', 'JavaScript'],
            'Frameworks': ['Django', 'React', 'ASP.NET Core'],
            'Databases': ['PostgreSQL', 'SQL Server'],
            'Tools': ['TensorFlow', 'DeepFace', 'TextBlob', 'Entity Framework Core'],
            'Soft Skills': ['Communication', 'Teamwork & Collaboration', 'Problem-solving', 'Emotional Intelligence'],
            'Languages Spoken': ['English (Fluent)', 'Hindi', 'Tamil'],
        }

        for order, (cat_name, skills) in enumerate(categories.items(), 1):
            category, created = TechCategory.objects.get_or_create(
                name=cat_name,
                defaults={'order': order, 'is_active': True}
            )
            action = 'Created' if created else 'Exists'
            self.stdout.write(f'  {action} category: {cat_name}')

            for skill_order, skill_name in enumerate(skills, 1):
                skill, created = TechStack.objects.get_or_create(
                    category=category,
                    name=skill_name,
                    defaults={'order': skill_order, 'is_active': True, 'level': 80}
                )
                action = 'Created' if created else 'Exists'
                self.stdout.write(f'    {action} skill: {skill_name}')

    def _create_education(self):
        education_data = [
            {
                'institution': 'Rathinam Global University',
                'degree': 'Bachelor of Engineering - Computer Science and Engineering',
                'year': '2022 - 2026',
                'description': 'CGPA: 8.50',
                'order': 1,
            },
            {
                'institution': 'Vidhya Vikas Higher Secondary School',
                'degree': 'Bio-Maths',
                'year': '2021 - 2022',
                'description': 'GPA: 88.3%',
                'order': 2,
            },
        ]

        for edu_data in education_data:
            edu, created = Education.objects.get_or_create(
                institution=edu_data['institution'],
                defaults=edu_data
            )
            action = 'Created' if created else 'Exists'
            self.stdout.write(f'  {action} education: {edu.degree} - {edu.institution}')

    def _create_experience(self):
        exp, created = Experience.objects.get_or_create(
            company='Embuzz Technologies Pvt. Ltd.',
            defaults={
                'role': 'Full-Stack Developer',
                'duration': '2024',
                'responsibilities': 'Successfully completed professional training in Embedded C Programming. Gained hands-on experience in microcontroller programming and developing real-time embedded systems.',
                'order': 1,
                'is_active': True,
            }
        )
        action = 'Created' if created else 'Exists'
        self.stdout.write(f'  {action} experience: {exp.role} @ {exp.company}')

    def _create_projects(self):
        # Get or create tags
        ai_tag, _ = ProjectTag.objects.get_or_create(name='AI/ML', defaults={'order': 1, 'is_active': True})
        web_tag, _ = ProjectTag.objects.get_or_create(name='Web Development', defaults={'order': 2, 'is_active': True})
        fullstack_tag, _ = ProjectTag.objects.get_or_create(name='Full-Stack', defaults={'order': 3, 'is_active': True})

        # Get tech stacks
        python = TechStack.objects.filter(name='Python').first()
        django = TechStack.objects.filter(name='Django').first()
        postgresql = TechStack.objects.filter(name='PostgreSQL').first()
        js = TechStack.objects.filter(name='JavaScript').first()
        html = TechStack.objects.filter(name='HTML').first()
        css = TechStack.objects.filter(name='CSS').first()
        csharp = TechStack.objects.filter(name='C#').first()
        aspnet = TechStack.objects.filter(name='ASP.NET Core').first()
        react = TechStack.objects.filter(name='React').first()
        sqlserver = TechStack.objects.filter(name='SQL Server').first()

        projects = [
            {
                'title': 'AI Movie Recommendation System',
                'short_description': 'AI-powered movie recommendation platform with personalized recommendations.',
                'description': 'Developed an AI-powered movie recommendation platform with personalized recommendations. Integrated sentiment analysis and emotion detection to enhance user recommendations. Designed a responsive user interface and managed data using PostgreSQL.',
                'is_featured': True,
                'order': 1,
                'tags': [ai_tag, web_tag],
                'tech_stack': [t for t in [python, django, postgresql, js, html, css] if t],
            },
            {
                'title': 'Bank Management System',
                'short_description': 'Full-stack banking application with secure authentication and role-based access.',
                'description': 'Developed a full-stack banking application with secure authentication and role-based access. Built RESTful APIs using ASP.NET Core Web API and Entity Framework Core. Developed an interactive frontend using React.js and integrated it with backend services.',
                'is_featured': True,
                'order': 2,
                'tags': [fullstack_tag, web_tag],
                'tech_stack': [t for t in [csharp, aspnet, react, sqlserver] if t],
            },
        ]

        for proj_data in projects:
            tags = proj_data.pop('tags')
            tech_stack = proj_data.pop('tech_stack')

            project, created = Project.objects.get_or_create(
                title=proj_data['title'],
                defaults=proj_data
            )

            if created:
                project.tags.set(tags)
                project.tech_stack.set(tech_stack)

            action = 'Created' if created else 'Exists'
            self.stdout.write(f'  {action} project: {project.title}')

    def _create_certifications(self):
        certs = [
            {
                'name': 'Prompt Engineering Data',
                'issuer': 'Coursera',
                'order': 1,
                'is_active': True,
            },
            {
                'name': 'Automation Developer Associate Training',
                'issuer': 'UiPath',
                'order': 2,
                'is_active': True,
            },
        ]

        for cert_data in certs:
            cert, created = Certification.objects.get_or_create(
                name=cert_data['name'],
                defaults=cert_data
            )
            action = 'Created' if created else 'Exists'
            self.stdout.write(f'  {action} certification: {cert.name} - {cert.issuer}')
