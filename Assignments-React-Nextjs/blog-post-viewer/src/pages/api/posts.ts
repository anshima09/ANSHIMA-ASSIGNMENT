import { NextApiRequest, NextApiResponse } from 'next';

const posts = [
  {
    id: 1,
    title: 'Understanding React Server Components',
    content: `React Server Components allow you to build modern, performant web apps with less client-side JavaScript. In this post, we explore how they work and how to use them in a Next.js app.`,
    author: 'Jane Doe',
    date: '2024-07-01',
  },
  {
    id: 2,
    title: 'Getting Started with Tailwind CSS',
    content: `Tailwind CSS is a utility-first CSS framework that makes it easy to build responsive UIs quickly. We'll walk through how to set it up and apply common styles.`,
    author: 'John Smith',
    date: '2024-07-02',
  },
  {
    id: 3,
    title: 'Next.js App Router: A Complete Guide',
    content: `The App Router in Next.js 13+ introduces a new file-based routing system with layouts, server components, and nested routes. This guide will walk you through all the essentials.`,
    author: 'Alex Lee',
    date: '2024-07-03',
  },
];

export default function handler(req: NextApiRequest, res: NextApiResponse) {
  res.status(200).json(posts);
}
