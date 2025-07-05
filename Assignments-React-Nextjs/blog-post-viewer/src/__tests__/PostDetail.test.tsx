import { render, screen } from '@testing-library/react';
import PostDetail from '../components/PostDetail';

test('shows fallback message', () => {
  render(<PostDetail post={null} />);
  expect(screen.getByText(/select a post/i)).toBeInTheDocument();
});

test('displays selected post', () => {
  const post = { id: 1, title: 'Post Title', content: 'Content here' };
  render(<PostDetail post={post} />);
  expect(screen.getByText('Post Title')).toBeInTheDocument();
  expect(screen.getByText('Content here')).toBeInTheDocument();
});
