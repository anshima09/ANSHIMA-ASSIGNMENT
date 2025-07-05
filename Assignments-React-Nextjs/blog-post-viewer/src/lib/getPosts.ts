export async function getPosts() {
  const res = await fetch('http://localhost:3000/api/posts');
  if (!res.ok) throw new Error('Failed to fetch posts');
  return res.json();
}
