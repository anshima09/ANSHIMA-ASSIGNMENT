'use client';

interface Post {
  id: number;
  title: string;
  content: string;
  author?: string;
  date?: string;
}

interface Props {
  post: Post | null;
}

export default function PostDetail({ post }: Props) {
  if (!post) {
    return (
      <div className="bg-white rounded-lg shadow p-6 text-gray-500 text-center">
        <p>Select a post to see the details.</p>
      </div>
    );
  }

  return (
    <div className="bg-white rounded-lg shadow p-6">
      <h2 className="text-2xl font-semibold text-gray-800 mb-2">{post.title}</h2>
      <p className="text-sm text-gray-400 mb-4">
        {post.author ?? 'Anonymous'} • {post.date ?? 'Unknown date'}
      </p>
      <p className="text-gray-700 leading-relaxed whitespace-pre-line">{post.content}</p>
    </div>
  );
}
