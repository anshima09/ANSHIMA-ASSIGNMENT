'use client';

import { useState } from 'react';
import PostList from '@/components/PostList';
import PostDetail from '@/components/PostDetail';

interface Post {
  id: number;
  title: string;
  content: string;
  author?: string;
  date?: string;
}

export default function PostsClient({ posts }: { posts: Post[] }) {
  const [selectedPost, setSelectedPost] = useState<Post | null>(null);

  return (
    <section className="min-h-screen bg-gray-50 py-12 px-4 sm:px-6 lg:px-8">
      <div className="max-w-5xl mx-auto">
        <header className="text-center mb-12">
          <h1 className="text-4xl font-semibold text-gray-800">Blog Post Viewer</h1>
          <p className="text-gray-500 mt-2">Browse and read selected blog posts.</p>
        </header>

        <div className="grid gap-10 md:grid-cols-2">
          <PostList posts={posts} onSelect={setSelectedPost} />
          <PostDetail post={selectedPost} />
        </div>
      </div>
    </section>
  );
}
