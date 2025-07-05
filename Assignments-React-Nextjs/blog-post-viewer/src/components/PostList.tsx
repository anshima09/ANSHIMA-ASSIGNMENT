'use client';

interface Post {
  id: number;
  title: string;
  content: string;
  author?: string;
  date?: string;
}

interface Props {
  posts: Post[];
  onSelect: (post: Post) => void;
}

export default function PostList({ posts, onSelect }: Props) {
  return (
    <div className="bg-white rounded-lg shadow p-6">
      <h2 className="text-xl font-medium text-gray-700 mb-4">Available Posts</h2>
      <ul className="space-y-3">
        {posts.map(post => (
          <li key={post.id}>
            <button
              className="w-full text-left px-4 py-2 rounded-md border border-gray-200 bg-gray-100 hover:bg-gray-200 text-gray-800 transition"
              onClick={() => onSelect(post)}
            >
              {post.title}
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
}
