export default function AgentProgress({ events }) {
  return (
    <div className="space-y-2">
      {events.map((event, index) => (
        <div
          key={index}
          className="text-green-400"
        >
          ✅ {event}
        </div>
      ))}
    </div>
  );
}