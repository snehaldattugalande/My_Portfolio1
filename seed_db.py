import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_site.settings')
django.setup()

from core.models import Profile, Stat, SkillCategory, Skill, Project, ProjectTech, Certification, SocialLink

def seed_db():
    print("Clearing existing data...")
    Profile.objects.all().delete()
    Stat.objects.all().delete()
    SkillCategory.objects.all().delete()
    Project.objects.all().delete()
    Certification.objects.all().delete()
    SocialLink.objects.all().delete()

    print("Seeding Profile...")
    Profile.objects.create(
        name="Snehal Galande",
        title="Data Engineer",
        subtitle="Building scalable architectures & intelligent pipelines.",
        greeting_code="// SNEHAL.INIT()",
        terminal_command="./execute_intro.sh",
        terminal_output="Hello, world! I engineer data ecosystems.",
        about_text="I am a passionate Data Engineer focused on transforming raw data into actionable insights. I design, build, and maintain robust, scalable data architectures and processing pipelines.",
        about_text_2="My expertise bridges the gap between software engineering and data science, ensuring data is reliable, accessible, and high-quality for downstream analytics and machine learning models.",
        email="hello@example.com",
        contact_message="I'm currently open for new opportunities to build scalable systems. Whether you have a question or just want to say hi, my inbox is always open!"
    )

    print("Seeding Stats...")
    Stat.objects.create(icon="fa-solid fa-database", icon_color="blue", value="10TB+", label="Data Processed", order=1)
    Stat.objects.create(icon="fa-solid fa-code-branch", icon_color="purple", value="50+", label="Pipelines Built", order=2)
    Stat.objects.create(icon="fa-solid fa-server", icon_color="blue", value="99.9%", label="Uptime", order=3)

    print("Seeding Skills...")
    lang_cat = SkillCategory.objects.create(name="Core Languages", order=1)
    Skill.objects.create(name="Python", category=lang_cat)
    Skill.objects.create(name="SQL", category=lang_cat)
    Skill.objects.create(name="Scala", category=lang_cat)
    Skill.objects.create(name="Bash", category=lang_cat)

    etl_cat = SkillCategory.objects.create(name="Processing & ETL", order=2)
    Skill.objects.create(name="Apache Spark", category=etl_cat)
    Skill.objects.create(name="Apache Kafka", category=etl_cat)
    Skill.objects.create(name="Airflow", category=etl_cat)
    Skill.objects.create(name="dbt", category=etl_cat)

    cloud_cat = SkillCategory.objects.create(name="Cloud & Databases", order=3)
    Skill.objects.create(name="AWS", category=cloud_cat)
    Skill.objects.create(name="Snowflake", category=cloud_cat)
    Skill.objects.create(name="PostgreSQL", category=cloud_cat)
    Skill.objects.create(name="Redis", category=cloud_cat)

    print("Seeding Projects...")
    p1 = Project.objects.create(
        title="Real-time Analytics Engine",
        description="Built a scalable real-time streaming pipeline processing 100K+ events/sec using Kafka and Spark Streaming.",
        github_url="#",
        order=1
    )
    ProjectTech.objects.create(name="Spark", project=p1)
    ProjectTech.objects.create(name="Kafka", project=p1)
    ProjectTech.objects.create(name="Python", project=p1)

    p2 = Project.objects.create(
        title="Automated ETL Platform",
        description="Designed an orchestrated ETL framework that reduced data processing time by 40% using Apache Airflow.",
        github_url="#",
        order=2
    )
    ProjectTech.objects.create(name="Airflow", project=p2)
    ProjectTech.objects.create(name="AWS", project=p2)
    ProjectTech.objects.create(name="Python", project=p2)

    p3 = Project.objects.create(
        title="Data Warehouse Modernization",
        description="Migrated legacy on-premise data warehouse to Snowflake. Implemented dbt for complex transformations.",
        github_url="#",
        order=3
    )
    ProjectTech.objects.create(name="Snowflake", project=p3)
    ProjectTech.objects.create(name="dbt", project=p3)
    ProjectTech.objects.create(name="SQL", project=p3)

    print("Seeding Certifications...")
    Certification.objects.create(
        title="SQL (Advanced) Certificate",
        issuer="HackerRank",
        icon="fa-solid fa-code",
        icon_color="blue",
        verify_url="https://www.hackerrank.com/certificates/3a40ea50d2f6",
        order=1
    )
    Certification.objects.create(
        title="Build Data Pipelines with Lakeflow Spark",
        issuer="Databricks",
        icon="fa-solid fa-bolt",
        icon_color="purple",
        verify_url="https://credentials.databricks.com/ff084b31-e716-49ff-90ac-b8565851b83f#acc.zd2hC1cJ",
        order=2
    )
    Certification.objects.create(
        title="Databricks Fundamentals",
        issuer="Databricks",
        icon="fa-solid fa-cubes",
        icon_color="blue",
        verify_url="https://credentials.databricks.com/be40bd42-82b7-476a-9ae0-6c8eacba8190#acc.eqOtvdWY",
        order=3
    )
    Certification.objects.create(
        title="Generative AI Fundamentals",
        issuer="Databricks",
        icon="fa-solid fa-robot",
        icon_color="purple",
        verify_url="https://credentials.databricks.com/150edb46-d6d9-4607-81a0-8cb9169e8297",
        order=4
    )
    Certification.objects.create(
        title="Reinvention with Agentic AI",
        issuer="Accenture (Credly)",
        icon="fa-solid fa-brain",
        icon_color="blue",
        verify_url="https://www.credly.com/badges/20178ffb-3417-499e-be8b-0ba5a44258b3",
        order=5
    )

    print("Seeding Social Links...")
    SocialLink.objects.create(platform="GitHub", url="#", icon="fa-brands fa-github", order=1)
    SocialLink.objects.create(platform="LinkedIn", url="#", icon="fa-brands fa-linkedin-in", order=2)
    SocialLink.objects.create(platform="Twitter", url="#", icon="fa-brands fa-twitter", order=3)

    print("Database seeding complete!")

if __name__ == "__main__":
    seed_db()
