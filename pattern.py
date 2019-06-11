SEED = '00100'
MAX_LENGTH = 300

def has_pattern_at(subject, i):
    for sequence_length in range(1, 1 + i // 2):
        right = subject[i - sequence_length: i]
        left = subject[i - 2 * sequence_length: i - sequence_length]
        if left == right and left[0] == subject[i]:
            return True
    return False

# Search a subject for a pattern. Look from right to left because
# patterns are more likely to occur there
def has_pattern(subject):
    for i in range (len(subject) - 2):
        if has_pattern_at(subject, len(subject) - 1 - i):
            return True
    return False

def increment(subject):
    i = len(subject) - 1;
    while subject[i] == '1':
        subject = subject[:i] + '0' + subject[i + 1:]
        i -= 1
        if i < 0:
            raise Exception("All possibilities exhausted")
    return subject[:i] + '1' + subject[i + 1:]

def main():
    subject = SEED;
    while len(subject) < MAX_LENGTH:
        while has_pattern(subject):
            subject = increment(subject)
        print(subject);
        subject += '0'

if __name__ == "__main__":
    main()
