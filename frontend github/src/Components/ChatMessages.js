const ChatMessages = ({ messages, typing }) => {
  return (
    <div className="chat-messages">
      {messages.map((msg, index) => (
        <div key={index} className={`message-row ${msg.isBot ? 'bot' : 'user'}`}>
          <img
            src={msg.isBot ? '/bot-avatar.png' : '/user-avatar.png'}
            className="avatar"
            alt={msg.isBot ? 'Bot' : 'You'}
          />
          <div className={`message-bubble ${msg.isBot ? 'bot' : 'user'}`}>
            <p>{msg.text}</p>
            <span className="timestamp">{msg.timestamp}</span>
          </div>
        </div>
      ))}
      {typing && (
        <div className="message-row bot">
          <img src="/bot-avatar.png" className="avatar" alt="Bot" />
          <div className="message-bubble bot typing">
            <span className="dot-flashing"></span>
          </div>
        </div>
      )}
    </div>
  );
};

export default ChatMessages;
