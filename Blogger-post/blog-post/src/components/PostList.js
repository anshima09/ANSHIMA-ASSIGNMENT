import styles from './PostList.module.css';
import Link from 'next/link';

export default function PostList({ posts }) {
  return (
    <div className={styles.wrapper}>
      <div className={styles.listContainer}>
        <h2 className={styles.title}>All Blog Posts</h2>
        {Array.isArray(posts) && posts.map((post) => (
          <Link key={post.id} href={`/posts/${post.id}`}>
            <div className={styles.postItem}>
              <h3 className={styles.postTitle}>{post.title}</h3>
            </div>
          </Link>
        ))}

      </div>
    </div>
  );
}
