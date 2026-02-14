---
layout: default
title: Md. Mahmudul Haque | Portfolio
---

<style>
:root {
  --bg: #f7f8fc;
  --card: #ffffff;
  --text: #1f2937;
  --muted: #6b7280;
  --accent: #4f46e5;
  --accent-soft: #e0e7ff;
  --line: #e5e7eb;
}

body {
  background: radial-gradient(circle at top right, #eef2ff, var(--bg) 40%);
  color: var(--text);
}

.portfolio {
  max-width: 960px;
  margin: 2rem auto 3rem;
  font-family: "Inter", "Segoe UI", Roboto, Arial, sans-serif;
  line-height: 1.6;
}

.hero {
  display: grid;
  grid-template-columns: 150px 1fr;
  gap: 1.5rem;
  align-items: center;
  background: linear-gradient(135deg, #ffffff 0%, #f8faff 100%);
  border: 1px solid var(--line);
  border-radius: 18px;
  padding: 1.5rem;
  box-shadow: 0 10px 30px rgba(31, 41, 55, 0.08);
}

.hero img {
  width: 150px;
  height: 150px;
  object-fit: cover;
  border-radius: 50%;
  border: 4px solid var(--accent-soft);
}

.hero h1 {
  margin: 0;
  font-size: 2rem;
}

.hero p {
  margin: 0.4rem 0;
  color: var(--muted);
}

.tagline {
  color: var(--text) !important;
  font-weight: 600;
}

.links {
  display: flex;
  flex-wrap: wrap;
  gap: 0.6rem;
  margin-top: 0.8rem;
}

.links a {
  text-decoration: none;
  color: var(--accent);
  background: var(--accent-soft);
  border: 1px solid #c7d2fe;
  padding: 0.35rem 0.65rem;
  border-radius: 999px;
  font-size: 0.9rem;
  transition: all 0.2s ease;
}

.links a:hover {
  transform: translateY(-1px);
  background: #c7d2fe;
}

.grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 1rem;
  margin-top: 1rem;
}

.card {
  background: var(--card);
  border: 1px solid var(--line);
  border-radius: 14px;
  padding: 1.1rem 1.2rem;
}

.card h2 {
  margin: 0 0 0.6rem;
  font-size: 1.05rem;
}

.card ul {
  margin: 0;
  padding-left: 1.15rem;
}

.full {
  grid-column: 1 / -1;
}

.small {
  color: var(--muted);
  font-size: 0.92rem;
}

@media (max-width: 760px) {
  .hero {
    grid-template-columns: 1fr;
    text-align: center;
  }

  .hero img {
    margin: 0 auto;
  }

  .links {
    justify-content: center;
  }

  .grid {
    grid-template-columns: 1fr;
  }
}
</style>

<div class="portfolio">
  <section class="hero">
    <img src="image/FB.jpg" alt="Profile photo of Md. Mahmudul Haque" />
    <div>
      <h1>Md. Mahmudul Haque</h1>
      <p class="tagline">Data Scientist • NLP & Computer Vision • M.Sc. Data Science @ TU Dortmund</p>
      <p>
        I build practical machine learning products, from NLP pipelines and summarization APIs to
        computer vision systems deployed on cloud and edge devices.
      </p>
      <div class="links">
        <a href="https://www.linkedin.com/in/md-mahmudul-haque-8a5484b2">LinkedIn</a>
        <a href="https://github.com/alcatraz47?tab=repositories">GitHub</a>
        <a href="https://medium.com/@arfanmahmud47/has-recommended">Medium</a>
        <a href="https://www.facebook.com/mahmud.arfan.alcatraz47">Facebook</a>
      </div>
    </div>
  </section>

  <section class="grid">
    <article class="card">
      <h2>About</h2>
      <p>
        Data science practitioner with 5+ years of research and industry experience.
        Strong interest in <strong>Natural Language Processing</strong>, with hands-on delivery across
        MLOps, APIs, model optimization, and production integration.
      </p>
    </article>

    <article class="card">
      <h2>Current Role</h2>
      <ul>
        <li>Data Science Working Student / Intern at <strong>Henkel AG & Co. KGaA</strong>, Düsseldorf</li>
        <li>M.Sc. in Data Science at <strong>Technical University Dortmund</strong></li>
      </ul>
    </article>

    <article class="card">
      <h2>Past Experience</h2>
      <ul>
        <li>Software Engineer (Part-time), Proxify AB (2023–2024)</li>
        <li>Data Scientist & Engineer, Eucaps Ltd. (2021–2022)</li>
        <li>Machine Learning Engineer, NybSys Pvt. Ltd. (2019–2021)</li>
      </ul>
    </article>

    <article class="card">
      <h2>Core Skills</h2>
      <ul>
        <li>Python, PyTorch, FastAPI, Spark, SQL</li>
        <li>NLP (summarization, text classification), Speech processing</li>
        <li>Computer Vision (detection, recognition, tracking)</li>
        <li>AWS (S3, Lambda, SageMaker, Redshift), Azure</li>
      </ul>
    </article>

    <article class="card full">
      <h2>Selected Projects</h2>
      <ul>
        <li><strong>Financial News Summarization:</strong> Built English news summarization pipeline and API for SMEs in Europe.</li>
        <li><strong>FaceNext:</strong> Contributed to face recognition-based access control system for web/mobile with cloud + edge deployment.</li>
        <li><strong>Emotion Recognition from Voice:</strong> Built deep learning pipeline using MFCC/Mel features and sequential models.</li>
        <li><strong>Rice Disease Detection:</strong> Capstone project with custom CNN + ResNet variants for disease classification.</li>
      </ul>
    </article>

    <article class="card">
      <h2>Publication</h2>
      <p>
        <strong>Data Mining Techniques to Categorize Single Paragraph Formed Self Narrated Stories</strong><br />
        ICT4SD, 2020.
      </p>
    </article>

    <article class="card">
      <h2>Recognition</h2>
      <p>
        8th place at Team Contest of <strong>NeurIPS AutoDL Challenge</strong>
        (Auto Speech Challenge), co-hosted by Google, Cha-Learn, and 4Paradigm.
      </p>
    </article>

    <article class="card full">
      <h2>Interests</h2>
      <p class="small">Travelling • Listening to music • Reading fiction • Formula 1</p>
    </article>
  </section>
</div>
