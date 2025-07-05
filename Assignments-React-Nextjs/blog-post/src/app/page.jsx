import Link from "next/link";
import styles from "./Home.module.css";

export default function Home() {
  return (
    <main className={styles.main}>
      <div className={styles.container}>
        <h1 className={styles.heading}>
          Welcome to the Blog Viewer ✨
        </h1>
        <p className={styles.description}>
          Explore all your favorite posts in one place. Click below to get started.
        </p>
        <Link
          href="/posts"
          className={styles.button}
        >
          View Blog Posts
        </Link>
      </div>
    </main>
  );
}