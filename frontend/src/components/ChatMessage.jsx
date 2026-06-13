export default function ChatMessage({
  role,
  content
}) {
  const isUser = role === "user";

  return (
    <div
      className={`p-4 rounded-xl mb-4 ${
        isUser
          ? "bg-blue-600 ml-auto max-w-xl"
          : "bg-gray-900 max-w-3xl"
      }`}
    >
      {content}
    </div>
  );
}