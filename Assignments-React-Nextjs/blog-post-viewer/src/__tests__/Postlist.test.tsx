import { render, screen, fireEvent } from '@testing-library/react';
import PostList from '../components/PostList';

const posts = [
  { id: 1, title: 'Test 1', content: 'A' },
  { id: 2, title: 'Test 2', content: 'B' },
];

test('renders post titles and handles click', () => {
  const onSelect = jest.fn();
  render(<PostList posts={posts} onSelect={onSelect} />);

  const first = screen.getByText('Test 1');
  fireEvent.click(first);

  expect(onSelect).toHaveBeenCalledWith(posts[0]);
});
