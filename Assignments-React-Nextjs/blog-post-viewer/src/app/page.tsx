import Image from "next/image";
import Link from "next/link";

export default function Home() {
  return (
    <main className="min-h-screen bg-gradient-to-br from-indigo-100 via-purple-100 to-pink-100 flex items-center justify-center p-6">
      <div className="bg-white shadow-xl rounded-2xl p-10 max-w-xl w-full text-center">
        <h1 className="text-4xl font-bold text-indigo-700 mb-6">
          Welcome to the Blog Viewer
        </h1>
        <p className="text-gray-600 mb-8">
          Browse all your favorite posts in one place. Click below to explore.
        </p>
        <Link
          href="/posts"
          className="inline-block bg-indigo-600 text-white px-6 py-3 rounded-lg hover:bg-indigo-700 transition"
        >
          View Blog Posts
        </Link>
      </div>
    </main>
  );
}
