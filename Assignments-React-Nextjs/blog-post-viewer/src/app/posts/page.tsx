import { getPosts } from '@/lib/getPosts';
import PostsClient from './PostsClient';

export default async function PostsPage() {
  const posts = await getPosts(); // ✅ Allowed here because it's a server component
  return <PostsClient posts={posts} />;
}
